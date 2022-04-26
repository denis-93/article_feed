from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwnerOrReadOnly
from .models import User, Article
from .serializers import UserSerializer, ArticleSerializer, ArticleCreateUpdateDeleteSerializer


class CreateUserView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleViewSet(ModelViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Article.objects.all()
        else:
            return Article.objects.filter(public=True)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ArticleSerializer
        else:
            return ArticleCreateUpdateDeleteSerializer

    def create(self, request, *args, **kwargs):
        if request.user.type == 'А':
            serializer = ArticleCreateUpdateDeleteSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=self.request.user)
                return Response(serializer.data, status=201)
        else:
            return Response({'Error': 'Не достаточно прав'}, status=403)
