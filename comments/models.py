from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

USER_MODEL = settings.AUTH_USER_MODEL


class Comment(models.Model):
    user = models.ForeignKey(
        verbose_name='Пользователь',
        to=USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    text = models.TextField(
        verbose_name='Текст',
        max_length=1000,
    )
    at_created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now=True,
    )
    content_type = models.ForeignKey(
        verbose_name='Тип контента',
        to=ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        return self.text


class SupportCommentsMixin(models.Model):
    comments = GenericRelation(
        to=Comment,
        object_id_field='object_id',
        content_type_field='content_type',
    )

    class Meta:
        abstract = True


__all__ = [
    'Comment',
    'SupportCommentsMixin',
]
