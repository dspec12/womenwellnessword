from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone


User = get_user_model()


class Author(models.Model):
    fullname = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    profile_picture = models.ImageField()
    bio = models.TextField()

    def __str__(self):
        return self.fullname


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title")
    overview = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk, "slug": self.slug})

    def save(self):
        if self.featured == True:
            items = Post.objects.filter(featured=True)
            for i in items:
                i.featured = False
                i.save()
        super().save()
