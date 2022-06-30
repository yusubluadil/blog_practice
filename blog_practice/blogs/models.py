from enum import auto
from django.db import models
from accounts.models import User

# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    created = models.DateField(auto_now = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blogs')
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
    
    def __str__(self) -> str:
        return f'{self.author} -- {self.title}'