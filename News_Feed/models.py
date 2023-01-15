from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    category = models.CharField(max_length= 12,verbose_name= "Post Category")

    def __str__(self):
        return  self.category

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creator')
    title = models.CharField(max_length=255, verbose_name='title')
    short_desc = models.CharField(max_length=30,verbose_name='description')
    text = models.TextField(verbose_name="Text")
    date = models.DateField(auto_now_add=True, verbose_name='Date')
    image = models.ImageField(upload_to='images', default='NONE', verbose_name='Photo/Picture')


    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Category")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Post")
    nickname = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name= "user's nickname")
    date = models.DateField(auto_now_add=True, verbose_name="Creation date")
    text = models.TextField(verbose_name="text")

    def __str__(self):
        return f'{self.post}|||{self.nickname}|||{self.date}'