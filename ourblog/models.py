from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
     return self.nombre

    def get_absolute_url(self):
     return reverse('home')
        


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    titulo_tag = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #Si borro a un user se borran todos las cosas relacionado a este ultimo.
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=200, default='coding')

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        #return reverse('artdetails', args=(str(self.id)))
        return reverse('home')
        
