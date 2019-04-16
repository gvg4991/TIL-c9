from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length = 40,blank=True)
    introduction = models.TextField(blank=True)
    image = ProcessedImageField(
        blank=True,
        upload_to='profile/images',
        processors = [ResizeToFill(300,300)],
        format = 'JPEG',
        options = {'quality':90},
        )
        
        
#followe 만들기
class User(AbstractUser): #models.Model보다 등록된 정보를 적게 가짐
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings') #한쪽은 팔로워,한쪽은 팔로잉
    
    
    