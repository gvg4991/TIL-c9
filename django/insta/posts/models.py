from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings


def post_image_path(instance,filename):
    return f'posts/images/{filename}'
    # return f'posts/{instance.content}/{instance.content}.jpg' #등록한 이름의 폴더명에 사진이 저장

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #외부키를 가지고옴, CASCADE(어떤게 삭제되면 그의 옵션들이 같이 삭제됨)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')


class Image(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE) #특정 포스터가 삭제됐을 때 어떻게 처리해줄지 정의
    file = ProcessedImageField(
        upload_to = post_image_path, #저장위치
        processors = [ResizeToFill(600,600)], #처리할 작업 목록
        format='JPEG', #저장 포맷
        options={'quality':90}, #옵션
        )


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #삭제되면 모든 댓글 삭제되는 기능
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()