from dataclasses import field
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from ..models import Post, Comment, Profile, Tag


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('caption',)


# class AuthorBookListSerialilzer(serializers.ModelSerializer):
#     genre = GenreSerializer(read_only=True, many=True)

#     class Meta:
#         model = Book
#         fields = '__all__'
class LoginSerializer(TokenObtainPairSerializer):

    default_error_messages = {
        "no_active_account": _("Invalid credentials")
    }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff

        return token

    def validate(self, attrs):
        return super().validate(attrs)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class CommentSerializer(serializers.ModelSerializer):
    user = AuthorSerializer()

    class Meta:
        model = Comment
        fields = ('text', 'user', 'is_archived', 'created_at')
        extra_kwargs = {
            'is_archived': {'read_only': True},
            'created_at': {'read_only': True},
        }

    def create(self, validated_data):
        request = self.context.get('request')
        post = Post.objects.filter(pk=request.kwargs['pk']).first()
        comment_instance = Comment(
            author=request.user, post=post, **validated_data)
        return comment_instance


class PostListSerialilzer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    author = AuthorSerializer()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        # ordering = ('-created_at',)
        extra_kwargs = {
            'comments': {'read_only': True}
        }


class PostSerialilzer(serializers.ModelSerializer):
    post_tags = TagSerializer(read_only=True, many=True)
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True, required=False, write_only=True)

    class Meta:
        model = Post
        fields = ('title', 'content', 'tags', 'image', 'post_tags', 'author')
        extra_kwargs = {
            "tags": {'write_only': True}
        }
    # def create(self, *args, **kwargs):``

    def validate(self, attrs):
        post = Post.objects.filter(title=attrs['title']).exists()
        if post:
            raise serializers.ValidationError(
                'A blog with this title already exists')
        return attrs

    def create(self, validated_data):
        print(validated_data)
        tags = validated_data.pop('tags')
        request = self.context.get('request')
        post_instance = Post(
            author=request.user, **validated_data)
        post_instance.save()
        for tag in tags:
            tag_instance, created = Tag.objects.get_or_create(
                defaults={'caption': tag['caption']}, caption__iexact=tag['caption'])
            post_instance.tags.add(tag_instance)
            post_instance.save()
        return post_instance
