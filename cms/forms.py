
from django import forms
from django_summernote.widgets import SummernoteWidget
from blog.models import Post, Author


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "overview", "body"]
        widgets = {"body": SummernoteWidget()}


class Editarticle(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "author", "overview", "body", "categories", "thumbnail", "published", "featured",]
        widgets = {"body": SummernoteWidget()}

class Editauthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["fullname", "display_name", "profile_picture", "bio"]
        widgets = {"bio": SummernoteWidget()}