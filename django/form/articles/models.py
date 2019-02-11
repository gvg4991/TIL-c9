from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField() #모델폼은 위의 타이틀과 콘텐츠의 정보를 바탕으로 작성됨
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    