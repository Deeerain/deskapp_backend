from django.db import models

from users.models import User
from comments.models import SupportCommentsMixin


APP_STATUS_CHOISE = (
    ('OPEN', 'Открыто'),
    ('CLOSED', 'Закрыто'),
    ('IN_WORK', 'В работе'),
)


class App(SupportCommentsMixin, models.Model):
    theme = models.CharField(
        verbose_name='Тема',
        max_length=100,
        null=True,
        default=None,
    )
    text = models.TextField(
        verbose_name='Текст',
        max_length=3000,
    )
    user = models.ForeignKey(
        verbose_name='Пользователь',
        to=User,
        on_delete=models.CASCADE,
        related_name='user',
    )
    status = models.CharField(
        verbose_name='Статус',
        max_length=30,
        choices=APP_STATUS_CHOISE,
        default=APP_STATUS_CHOISE[0][1],
    )
    at_created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        blank=True
    )
    at_updated = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self) -> str:
        return f'{ self.theme or "Без темы"} {self.user}'
