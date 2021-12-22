from django.db import models

from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from django.utils import timezone


# Creating User model
class User(models.Model):
    first_name=models.CharField(max_length=100,verbose_name="First Name")
    last_name=models.CharField(max_length=100,verbose_name="Last Name")
    #Return user name and surname
    def __str__(self):
        return self.first_name + ' ' + self.last_name


# Creating Blog model
class Blog(models.Model):
    description=models.CharField(max_length=100,verbose_name="Blog Başlığı:")
    blog_content=RichTextField(verbose_name="Blog İçeriği:")
    cover_photo=models.FileField(upload_to='images/',verbose_name="Kapak Fotoğrafı:")
    blog_author=models.ForeignKey('auth.user',on_delete=CASCADE,verbose_name="Blog Yazarı:",related_name="posts")
    created_date=models.DateTimeField(default=timezone.now, verbose_name='Created Date')
    populer= models.BooleanField(default=False,verbose_name="Popüler?")
    #Return blog descripton
    def __str__(self):
        return self.description


class Comment(models.Model):
    name=models.CharField(max_length=500,verbose_name="İsim")
    post=models.ForeignKey(Blog,related_name="comments",on_delete=models.CASCADE)
    content=models.TextField(max_length=500,verbose_name="Yorum:")



   





