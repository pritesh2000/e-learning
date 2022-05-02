from django.db import models

# Create your models here.

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    c_id = models.AutoField(primary_key=True)
    cat = models.CharField(max_length=10)
    c_desc = models.CharField(max_length=1000)
    c_title = models.CharField(max_length=50)
    c_image = models.ImageField(upload_to="c_images/", default="")

    def __str__(self):
        return self.c_title

class Video(models.Model):
    v_id = models.AutoField(primary_key=True)
    v_title = models.CharField(max_length=100)
    v_cat = models.CharField(max_length=10)
    v_desc = models.CharField(max_length=1000)
    url = models.CharField(max_length=50)
    v_image = models.ImageField(upload_to="v_images/", default="")

    def __str__(self):
        return self.v_title