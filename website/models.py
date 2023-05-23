from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    is_menu = models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class FlashNews(models.Model):
    title=models.CharField(max_length=250)
    timestamp=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Slider(models.Model):
    slideImage=models.ImageField(upload_to='slider/')
    slideeHeader=models.CharField(max_length=50)
    slideTitle=models.CharField(max_length=100)
    slideSubtitle=models.CharField(max_length=200)
    slideBottomtitle=models.CharField(max_length=100)

    def __str__(self):
        return self.slideeHeader


class Card(models.Model):
    CardTitle=models.CharField(max_length=150)
    CardBottomTitle=models.CharField(max_length=100)
    CardImage=models.ImageField(upload_to='card/')

class BreakingNews(models.Model):
     newsImage=models.ImageField(upload_to='breakingnews/')
     newsHeader=models.CharField(max_length=100)
     newsinfo=models.CharField(max_length=50)
     newstitle=models.CharField(max_length=100)

class video(models.Model):
    VideoImage=models.ImageField(upload_to='video/')
    videoTitle=models.CharField(max_length=100)

    def __str__(self):
        return self.videoTitle