from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title   #post object로 뜨지않고 title을 보여줌
    
# 1. Creat
# post = Post(title='hello', content='world!')
# post.save()

# 2. Read
# 2.1. All
# posts = Post.objects.all() 포스트 데이터 베이스를 포스츠라는 변수에 저장
# 2.2. Get one
# post = Post.objects.get(pk=1) 장고는 id가 아니라 pk를 사용
# 2.3. filter (WHERE)
# posts = Post.objects.filter(title='Hello').all()
# post = Post.objects.filter(title='Hello').first()
# 2.4. Like
# posts = Post.objects.filter(title__contains='He').all()
# 2.5. orser_by (정렬)
# posts = Post.objects.order_by('title').all()  <-오름차순
# posts = Post.objects.order_by('-title').all() <-내임차순
# 2.6. offset & limit
# [offset:offset+limit]
# posts = Post.objects.all()[1:2]   <-오프셋 1만큼, 리미트 2만큼

# 3. Delete
# post = Post.objects.get(pk=2)
# post.delete()

# 4. Update
# post = Post.objects.get(pk=1) <- hello
# post.title = 'yo'             <- 인스턴스 yo
# post.save()                   <- yo