
from django.views.generic import ListView, TemplateView, View
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from blog.models import Post
from users.models import CustomUser
from django.contrib.auth import get_user_model

class AboutPageView(ListView):
    model = CustomUser
    template_name = "about.html"