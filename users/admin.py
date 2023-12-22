from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group

from users import models


class PositionInline(admin.StackedInline):
    model = models.Position
    extra = 1


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (PositionInline,)


@admin.register(models.Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('departament',)


@admin.register(models.User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'position',
                    'last_login')

    list_filter = ('position__departament', 'is_active')

    fieldsets = (
        ('Пользователь', {'fields': ('username', 'first_name', 'last_name',
                                     'email', 'telephone', 'password')}),
        ('Доступы', {'fields': ('is_active', 'is_superuser', 'is_staff',
                                'user_permissions')}),
        ('Штат', {'fields': ('position', 'last_login')}),
    )
