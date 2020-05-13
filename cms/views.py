from django.shortcuts import render
from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.decorators import login_required
from .forms import PostForm, Editarticle, Editauthor

from blog.models import Post, Author, Category

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
    form_class = Editarticle


class CmsEditAuthor(LoginRequiredMixin, UpdateView):
    model = Author
    template_name = "cms_edit_author.html"
    fields = ["fullname", "display_name", "profile_picture", "bio"]


class CmsEditCategory(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "cms_edit_category.html"
    fields = ["title"]


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
    fields = [
        "title",
        "author",
        "overview",
        "body",
        "categories",
        "thumbnail",
        "published",
        "featured",
    ]
    widgets = {"body": SummernoteWidget()}


class CmsNewAuthor(LoginRequiredMixin, CreateView):
    model = Author
    template_name = "cms_new_author.html"
    fields = ["fullname", "display_name", "profile_picture", "bio"]


class CmsNewCategory(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "cms_new_category.html"
    fields = ["title"]
