from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meme(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='uploads',height_field='image_height',width_field='image_width',)
    image_height = models.PositiveIntegerField(default=200)
    image_width=models.PositiveIntegerField(default=200)


    def __str__(self):
        return self.title