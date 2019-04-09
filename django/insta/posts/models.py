from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


def post_image_path(instance,filename):
    return f'posts/images/{filename}'
    # return f'posts/{instance.content}/{instance.content}.jpg' #등록한 이름의 폴더명에 사진이 저장

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        upload_to = post_image_path, #저장위치
        processors = [ResizeToFill(600,600)], #처리할 작업 목록
        format='JPEG', #저장 포맷
        options={'quality':90}, #옵션
        )