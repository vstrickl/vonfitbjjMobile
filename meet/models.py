from django.db import models

# Create your models here.
class Header(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.sub_title}"

class SocialMenu(models.Model):
    social = models.CharField(max_length=200, null=True, blank=True)
    font_awesome = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.social
    
class Menu(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title