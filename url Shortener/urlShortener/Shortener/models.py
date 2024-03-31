from django.db import models

# Create your models here.
# class Url(models.Model):
#     UrlInput = models.CharField(max_length=10000)
#     uuid = models.CharField(max_length=10)

#     from django.db import models

class Url(models.Model):
    link = models.URLField()
    uuid = models.CharField(max_length=10)



