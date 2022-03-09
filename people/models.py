from django.db import models

# Create your models here.
import book
from book.models import BookInfo


class PeopleInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    sex = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
    book_id = models.ForeignKey(BookInfo, on_delete=models.CASCADE, default=0)
