

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import UserSerializer, PostListSerialilzer, LoginSerializer, PostSerialilzer, CommentSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action, permission_classes
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from ..models import Post, Comment, Profile, Tag

from .renderer import CustomRenderer
from rest_framework_simplejwt.views import TokenObtainPairView


from django.conf import settings as app_settings
STATUS = app_settings.STATUS_CODES


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class LoginAPIView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            print(serializer.is_valid())
            if serializer.is_valid():
                return Response({
                    "success": True,
                    'status': STATUS.get('success', ''),
                    "token": serializer.validated_data,
                    "detail": "Login success"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "success": False,
                'status': STATUS.get('error', ''),
                # "token": serializer.errors,
                "detail":  "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)


login_view = LoginAPIView.as_view()
register_view = RegisterAPIView.as_view()


class BlogListAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:

            return Response({
                "success": True,
                'status': STATUS.get('success', ''),
                "data": context,
                "detail": "Data Retrived"}, status=status.HTTP_200_OK)
        except:
            return Response({
                "success": False,
                'status': STATUS.get('error', ''),
                "data": {},
                "detail":  "Error Fetching Data"}, status=status.HTTP_501_NOT_IMPLEMENTED)


home_views = BlogListAPIView.as_view()


# class BookListViewAPIView(ListAPIView):
#     queryset = Book.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = PostListSerialilzer
#     pagegination_class = StandardResultsSetPagination


# book_list_view = BookListViewAPIView.as_view()

class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialilzer
    permission_classes = (IsAuthenticated,)
    renderer_classes = (CustomRenderer,)


class PostListViewAPIView(ListAPIView):
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PostListSerialilzer
    pagegination_class = StandardResultsSetPagination
    renderer_classes = (CustomRenderer,)


post_create_view = PostCreateView.as_view()
post_list_view = PostListViewAPIView.as_view()


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PostListSerialilzer
    renderer_classes = (CustomRenderer,)


post_detail_view = PostDetailAPIView.as_view()


class CommentCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    renderer_classes = (CustomRenderer,)
    permission_classes = (IsAuthenticated,)
    pagegination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        comments = Comment.objects.filter(pk=kwargs['pk'])
        self.check_object_permissions(request, request.user)
        serializer = CommentSerializer(data=request.data, many=True)

        return Response({"data": serializer.validated_data}, status=status.HTTP_200_OK)



class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    renderer_classes = (CustomRenderer,)
    permission_classes = (IsAuthenticated,)
    pagegination_class = StandardResultsSetPagination


comment_list_view = CommentListAPIView.as_view()
comment_view = CommentCreateAPIView.as_view()
