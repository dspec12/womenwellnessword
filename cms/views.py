from django.shortcuts import render
from django.apps import apps

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required()
def cms_index(request):
    return render(request, "cms_index.html", context={})
