from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Photo(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='photo_posts')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, default='photos/no_image.png')
    text =models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('photo:post_detail', args=[str(self.id)])