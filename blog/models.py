from django.db import models
from markdownx.models import MarkdownxField
import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    description =  MarkdownxField()
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(default=datetime.date.today)
