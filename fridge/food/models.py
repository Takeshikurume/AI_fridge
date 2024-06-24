from django.db import models

class BaseManager(models.Manager):
   def get_or_none(self, **kwargs):
       """
       検索にヒットすればそのモデルを、しなければNoneを返します。
       """
       try:
           return self.get_queryset().get(**kwargs)
       except self.model.DoesNotExist:
           return None

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    num = models.CharField(max_length=255)
    date = models.CharField(max_length=255)

class Document(models.Model):
    # objects = BaseManager()
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='documents/', default='defo')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    output = models.ImageField(default = 'output/output.jpg')