from django.shortcuts import render
from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django_summernote.widgets import SummernoteWidget
from django.forms.widgets import SelectMultiple
from django.contrib.auth.decorators import login_required
from .forms import PostForm, EditArticle, EditAuthor, NewArticle

from blog.models import Post, Author, Category
from users.models import CustomUser
from invitations.models import Invitation

from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    View,
    CreateView,
    UpdateView,
    DeleteView,
)


@login_required()
def cms_index(request):
    return render(request, "cms_index.html", context={})


# @login_required()
# def cms_articles(request):
#     return render(request, "cms_articles.html", context={})

# Blog Views
class CmsArticles(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        get_articles = Post.objects.all().order_by("-timestamp")
        context = {"object_list": get_articles}

        return render(request, "cms_articles.html", context)


class CmsAuthors(LoginRequiredMixin, ListView):
    queryset = Author.objects.all()
    template_name = "cms_authors.html"


class CmsCategories(LoginRequiredMixin, ListView):
    queryset = Category.objects.all()
    template_name = "cms_categories.html"


class CmsEditArticle(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "cms_edit_article.html"
    form_class = EditArticle
    success_url = reverse_lazy("articles")


class CmsEditAuthor(LoginRequiredMixin, UpdateView):
    model = Author
    template_name = "cms_edit_author.html"
    fields = ["fullname", "display_name", "profile_picture", "bio"]
    success_url = reverse_lazy("authors")


class CmsEditCategory(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "cms_edit_category.html"
    fields = ["title"]
    success_url = reverse_lazy("categories")


class CmsDeleteArticle(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "cms_delete_article.html"
    success_url = reverse_lazy("articles")


class CmsDeleteAuthor(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = "cms_delete_author.html"
    success_url = reverse_lazy("authors")


class CmsDeleteCategory(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "cms_delete_category.html"
    success_url = reverse_lazy("categories")


class CmsNewArticle(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "cms_new_article.html"
    form_class = NewArticle
    success_url = reverse_lazy("articles")


class CmsNewAuthor(LoginRequiredMixin, CreateView):
    model = Author
    template_name = "cms_new_author.html"
    fields = ["fullname", "display_name", "profile_picture", "bio"]
    success_url = reverse_lazy("authors")


class CmsNewCategory(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "cms_new_category.html"
    fields = ["title"]
    success_url = reverse_lazy("categories")


# Users Views
class CmsUsers(LoginRequiredMixin, ListView):
    queryset = CustomUser.objects.all().filter(is_superuser=False)
    template_name = "cms_users.html"


class CmsDeleteUser(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "cms_delete_user.html"
    success_url = reverse_lazy("users")


class CmsInvites(LoginRequiredMixin, ListView):
    queryset = Invitation.objects.all()
    template_name = "cms_invites.html"
