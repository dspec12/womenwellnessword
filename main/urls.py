from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog.views import index, blog, post_detail, category

urlpatterns = [
    # Admin
    path("summernote/", include("django_summernote.urls")),
    path("admin/", admin.site.urls),
    # path("godmode/", godmode, name="godmode" )
    # Pages
    path("", index, name="home"),
    # Blog
    path("blog/", blog, name="blog"),
    path("blog/<int:pk>/<slug:slug>", post_detail, name="post_detail"),
    path("blog/category/<str:post_cat>", category, name="category"),
]