from django.db import models
from datetime import datetime

class DateMixin(models.Model):
    created_at = models.DateTimeField(default=datetime.now) 
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    
    class Meta:
        abstract = True


class Banner(DateMixin):
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banners')

    def __str__(self):
        return self.text


class Project(DateMixin):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects')

    def __str__(self):
        return self.title


class Partner(DateMixin):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners')

    def __str__(self):
        return self.name


class Video(DateMixin):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos')

    def __str__(self):
        return self.title
    

class Contact(DateMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.name
    