from django.conf import settings


def discus_app(request):
    return {"DISQUS_APP": settings.DISQUS_APP}
