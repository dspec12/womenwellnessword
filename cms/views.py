from django.shortcuts import render


def cms_index(request):
    return render(request, "cms_index.html", context={})
