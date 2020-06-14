from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import AboutPageView
from blog.views import index, blog, post_detail, category
from .override_views import SendInvite
from cms.views import (
    cms_index,
    CmsArticles,
    CmsAuthors,
    CmsCategories,
    CmsEditArticle,
    CmsEditAuthor,
    CmsEditCategory,
    CmsDeleteArticle,
    CmsDeleteAuthor,
    CmsDeleteCategory,
    CmsNewArticle,
    CmsNewAuthor,
    CmsNewCategory,
    CmsUsers,
    CmsDeleteUser,
    CmsInvites,
)

urlpatterns = [
    # Admin
    path("summernote/", include("django_summernote.urls")),
    path("admin/", admin.site.urls),
    # path("invitations/", include("invitations.urls", namespace="invitations")),
    #  CMS
    path("godmode/", cms_index, name="godmode"),
    # About Page
    path("about/", AboutPageView.as_view(), name="about"),
    # CMS Users
    path("godmode/users", CmsUsers.as_view(), name="users"),
    path(
        "godmode/users/delete/<int:pk>/",
        CmsDeleteUser.as_view(),
        name="cms_delete_user",
    ),
    path("godmode/invites/", CmsInvites.as_view(), name="invites"),
    path(
        "godmode/invites/delete/<int:pk>/",
        CmsDeleteCategory.as_view(),
        name="cms_delete_invite",
    ),
    # CMS Blog
    path("godmode/articles", CmsArticles.as_view(), name="articles"),
    path(
        "godmode/articles/edit/<int:pk>/",
        CmsEditArticle.as_view(),
        name="cms_edit_article",
    ),
    path(
        "godmode/articles/delete/<int:pk>/",
        CmsDeleteArticle.as_view(),
        name="cms_delete_article",
    ),
    path("godmode/articles/new/", CmsNewArticle.as_view(), name="cms_new_article",),
    path("godmode/authors", CmsAuthors.as_view(), name="authors"),
    path(
        "godmode/authors/edit/<int:pk>/",
        CmsEditAuthor.as_view(),
        name="cms_edit_author",
    ),
    path(
        "godmode/authors/delete/<int:pk>/",
        CmsDeleteAuthor.as_view(),
        name="cms_delete_author",
    ),
    path("godmode/authors/new/", CmsNewAuthor.as_view(), name="cms_new_author",),
    path("godmode/categories", CmsCategories.as_view(), name="categories"),
    path(
        "godmode/categories/edit/<int:pk>/",
        CmsEditCategory.as_view(),
        name="cms_edit_category",
    ),
    path(
        "godmode/categories/delete/<int:pk>/",
        CmsDeleteCategory.as_view(),
        name="cms_delete_category",
    ),
    path("godmode/categories/new/", CmsNewCategory.as_view(), name="cms_new_category",),
    # Auth
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("allauth.urls")),
    # Pages
    path("", index, name="home"),
    # Blog
    path("blog/", blog, name="blog"),
    path("blog/<int:pk>/<slug:slug>", post_detail, name="post_detail"),
    path("blog/category/<str:post_cat>", category, name="category"),
    # Django-Invites
    # Override url for django-invatations.SendInvite
    path("invitations/send-invite/", SendInvite.as_view(), name="send-invite"),
    path("invitations/", include("invitations.urls", namespace="invitations")),
]
