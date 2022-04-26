from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User, Article


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'type')
        read_only_fields = ('id',)

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, data):
        user = User.objects.create_user(**data)
        user.set_password(data['password'])
        user.save()
        return user


class ArticleSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='email', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'author', 'create_at')


class ArticleCreateUpdateDeleteSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Article
        fields = ('title', 'text', 'author', 'public')
        read_only_fields = ('author',)
