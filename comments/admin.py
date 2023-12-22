from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Comment


class CommentInline(GenericStackedInline):
    model = Comment
    extra = 1


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_link', 'at_created',
                    'content_type', 'object_link')
    list_filter = ('at_created', 'content_type')

    @admin.display(description='Сылка на объект')
    def object_link(self, instance: Comment):
        url = reverse('admin:%s_%s_change' % (
            instance.content_type.app_label,
            instance.content_type.model),
            args=[instance.object_id]
        )
        return mark_safe(f'<a href="{url}">{instance.content_object}</a>')

    @admin.display(description='Пользователь')
    def user_link(self, instance: Comment):
        user_app_label = instance.user._meta.app_label
        user_model_name = instance.user._meta.model_name

        url = reverse('admin:%s_%s_change' % (
            user_app_label,
            user_model_name),
            args=[instance.user.pk]
        )
        return mark_safe(f'<a href="{url}">{instance.user}</a>')