from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title")
    overview = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

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
