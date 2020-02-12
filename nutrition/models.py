from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Post(models.Model):
     subject=models.CharField(max_length=150)
     author=models.ForeignKey(
          get_user_model(),
          on_delete=models.CASCADE,)
     body=models.TextField()
     date=models.DateTimeField(auto_now_add=True)
     def __str__(self):
        return self.subject
     def get_absolute_url(self):
             return reverse('post_detail',args=[str(self.id)])