from django.db import models
from django.conf import settings
from django.conf.urls.static import static
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
             
class Nutrifile(models.Model):
    name=models.CharField(max_length=100,null=True)
    detail=models.CharField(max_length=2000,null=True)
    image=models.ImageField()
    serving_size=models.DecimalField(max_digits=8,decimal_places=1)
    calories=models.DecimalField(max_digits=8,decimal_places=1)
    total_fat=models.DecimalField(max_digits=8,decimal_places=1)
    protein=models.DecimalField(max_digits=8,decimal_places=1)
    cholestrol=models.DecimalField(max_digits=8,decimal_places=1)
    carbohydrates=models.DecimalField(max_digits=8,decimal_places=1)
    fiber=models.DecimalField(max_digits=8,decimal_places=1)

    
    def __str__(self):
        return self.name    
    