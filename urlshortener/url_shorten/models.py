from django.db import models

# Create your models here.

class url_shorten(models.Model):
    original_link = models.CharField(max_length=400)
    gen_link = models.CharField(max_length=15)