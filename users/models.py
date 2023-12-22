from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=50,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self) -> str:
        return self.name


class Position(models.Model):
    departament = models.ForeignKey(
        verbose_name='Отдел',
        to=Department,
        on_delete=models.CASCADE,
        related_name='departments',
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=50,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    position = models.ForeignKey(
        verbose_name='Позиция',
        to=Position,
        on_delete=models.SET_NULL,
        related_name='position',
        null=True,
    )
    telephone = models.CharField(
        verbose_name='Номер телефона',
        max_length=12,
        db_index=True,
        unique=True,
        null=True,
    )

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
