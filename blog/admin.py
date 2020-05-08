from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Author, Category, Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("body",)


admin.site.register(Author,)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
