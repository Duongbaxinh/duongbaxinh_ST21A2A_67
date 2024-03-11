from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null = True)
    audio = models.FileField(upload_to='media/music',null=True)
    def __str__(self):
        return f"{self.title}"

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.FileField(null= True)

class Music(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.FileField(null = True)
    musicfile = models.FileField(null= True)

class NhatKy(models.Model):
    date = models.DateTimeField(auto_created=True)
    content = models.CharField(max_length=1000)
    image = models.ImageField(null = True)


