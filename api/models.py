from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager


USER_TYPE_CHOISES = (
    ('П', 'Подписчик'),
    ('А', 'Автор'),
)

class User(AbstractUser):

    email = models.EmailField(verbose_name='Эл. почта', unique=True)
    type = models.CharField(verbose_name='Тип пользователя', choices=USER_TYPE_CHOISES, max_length=1, default='П')
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"
        ordering = ('email',)


class Article(models.Model):

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    text = models.TextField(verbose_name='Текст статьи')
    author = models.ForeignKey(User, verbose_name='Автор статьи', on_delete=models.CASCADE)
    public = models.BooleanField(verbose_name='Публичность')
    create_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
