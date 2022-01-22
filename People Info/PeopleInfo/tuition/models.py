from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from random import choices
from turtle import title
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    content=models.TextField()
    def __str__(self):
        return self.name

class Subject(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Class_in(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    CAREGORY=(
        ('teacher','teacher'),
        ('student','student'),
    )
    MEDIUM=(
        ('bangla','bangla'),
        ('english','english'),
        ('urdu','urdu'),
        ('hindi','hindi'),
    )
    user= models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,null=True
    )
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    slug=models.CharField(max_length=100,default=title)
    eamil=models.EmailField(max_length=100)
    salary=models.FloatField(max_length=50)
    details=models.TextField(max_length=30)
    availabe=models.BooleanField()
    catagory=models.CharField(max_length=100,choices=CAREGORY)
    created_at=models.DateTimeField(default=now)
    image=models.ImageField(default='default.jpg', upload_to='tuition/images')
    MEDIUM=MultiSelectField(max_length=100,max_choices=4,choices=MEDIUM,default='bangla')
    subject=models.ManyToManyField(Subject, related_name='subject_set')
    class_in=models.ManyToManyField(Class_in, related_name='class_set')
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args, **kwargs)
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
    
