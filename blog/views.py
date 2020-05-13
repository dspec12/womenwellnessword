from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    View,
    CreateView,
    UpdateView,
    DeleteView,
)


def get_category_count():
    queryset = Post.objects.values("categories__title").annotate(
        Count("categories__title")
    )
    return queryset


def index(request):
    featured = Post.objects.filter(featured=True, published=True)
    latest = Post.objects.filter(published=True).order_by("-timestamp")[0:3]
    context = {"featured": featured, "latest": latest}
    return render(request, "index.html", context)


def blog(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by("-timestamp")[:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        "queryset": paginated_queryset,
        "most_recent": most_recent,
        "page_request_var": page_request_var,
        "category_count": category_count,
    }
    return render(request, "blog.html", context)


def post_detail(request, pk, slug):
    category_count = get_category_count()
    most_recent = Post.objects.order_by("-timestamp")[:3]
    post = get_object_or_404(Post, pk=pk, slug=slug)
    context = {
        "post": post,
        "most_recent": most_recent,
        "category_count": category_count,
    }
    return render(request, "post.html", context)


def category(request, post_cat):
    category_count = get_category_count()
    most_recent = Post.objects.order_by("-timestamp")[:3]
    post_list = Post.objects.filter(categories__title=post_cat)
    paginator = Paginator(post_list, 4)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        "queryset": paginated_queryset,
        "most_recent": most_recent,
        "page_request_var": page_request_var,
        "category_count": category_count,
    }
    return render(request, "blog.html", context)
