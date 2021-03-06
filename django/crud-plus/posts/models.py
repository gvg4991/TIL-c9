from django.db import models

# Create your models here.
class Post(models.Model):   #Post 클래스를 생성
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title   #post object로 뜨지않고 title을 보여줌
        
# Post : Comment = 1 : N
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #외부 다른테이블의 키값을 가지고 와서 저장함
    content = models.TextField()
    
    # on_delete 옵션
    # 1. CASCADE : 부모가 삭제되면, 자기 자신도 삭제. ex) 포스트가 사라지면 댓글도 같이 사라짐
    # 2. PROTECT : 자식이 존재하면, 부모 삭제 불가능.
    # 3. SET_NULL : 부모가 삭제되면, 자식의 부모 정보를 NULL로 변경
    