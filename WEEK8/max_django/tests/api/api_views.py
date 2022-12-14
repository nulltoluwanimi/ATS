

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import UserSerializer, BookListSerialilzer, AuthorSerializer
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

from ..models import Book, Author, BookInstance, Genre

# from rest_framework_simplejwt.views import TokenObtainPairView


from django.conf import settings as app_settings

from tests.api import serializers
STATUS = app_settings.STATUS_CODES


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


register_view = RegisterAPIView.as_view()


class HomeAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            # Generate counts of some of the main objects
            num_books = Book.objects.all().count()
            num_instances = BookInstance.objects.all().count()
            num_visits = request.session.get('num_visits', 0)
            request.session['num_visits'] = num_visits + 1

            # Available books (status = 'a')
            num_instances_available = BookInstance.objects.filter(
                status__exact='a').count()
            num_genre = Genre.objects.all().count()
            # num_books = Book.objects.all().count()

            # The 'all()' is implied by default.
            num_authors = Author.objects.count()

            context = {
                'num_books': num_books,
                'num_instances': num_instances,
                'num_instances_available': num_instances_available,
                'num_authors': num_authors,
                'num_genre': num_genre,
                "num_visits": num_visits
            }

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


home_views = HomeAPIView.as_view()


class BookListViewAPIView(ListAPIView):
    queryset = Book.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BookListSerialilzer
    pagegination_class = StandardResultsSetPagination


book_list_view = BookListViewAPIView.as_view()


class AuthorListViewAPIView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AuthorSerializer
    pagegination_class = StandardResultsSetPagination


author_list_view = AuthorListViewAPIView.as_view()
