from django.contrib import admin

from applications import models as applications_models
from comments.admin import CommentInline


@admin.register(applications_models.App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('theme', 'user', 'status', 'at_updated', 'at_created')
    list_filter = ('status', 'at_created')
    list_editable = ('status',)
    inlines = (CommentInline,)
