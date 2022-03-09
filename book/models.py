from django.db import models

# Create your models here.
class BookInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False, default="")
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)
