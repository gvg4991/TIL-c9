from django.db import models

# Create your models here.

# 테이블 생성
class Post(models.Model):
    title = models.TextField()
    
    
# 용어 정리
# class Post: 장고-model, DB-테이블
# post = Post(): 장고-인스턴스 or 오브젝트, DB-레코드 or Row
# title: 장고-Field, DB-Column

# 마이그레이션
# ./manage.py makemigrations
# ./manage.py migrate

# pip install django_extensions
# ./manage.py shell_plus

# CRUD

# 1. Create
# 방법 1
# post = Post(title = 'yo-1')
# post.save() : DB에 인스턴스 저장
# 방법 2★
# post2 = Post.objects.create(title='yo-2') #한줄로 축약 가능
# 방법 3
# post3 = Post()
# post3.title = 'yo-3' #필드를 따로 분할하여 작성 가능
# post3.title = 'yo-3!!!' #수정 가능
# post3.save()

# 2. Read
# 2-1. All
# posts = Post.objects.all() #모든 정보를 posts라는 변수에 넣음
# 2-2. One
# 방법 1
# post = Post.objects.get(id=1) #id대신 pk가능, title='yo-1'로도 가지고 올 수 있음
# 방법 2 (view.py 한정)
# from django.shortcuts import het_objects_or_404
# post = get_object_or_404(Post, id=1) #id대신 pk가능, title='yo-1'로도 가지고 올 수 있음
# 방법 3
# Post.objects.filter(pk=1) #조건(pk=1)에 맞는 데이터를 리스트 형식으로 가지고옴
# Post.objects.filter(pk=1)[0] 또는 Post.objects.filter(pk=1).first()로 하나의 값을 가지고 옴
# 2-3. where(filter)
# posts = Post.objects.filter(title='yo-1')
# post = Post.objects.filter(title='yo-1').first() #또는 [0]

    # LIKE
    # posts = Post.objects.filter(title__contain='-1') #-1이 포함된 데이터를 가지고옴
    
    # order_by
    # Post.objects.order_by('title') #오름차순
    # Post.objects.order_by('-title') #내림차순
    
    # offset & limit
    # Post.objects.all()[0] -> offset 0(앞에 빼는 수) limit 1
    # Post.objects.all()[1] -> offset 1 limit 1
    # Post.objects.all()[1:3] -> offset 1 limit 2
    # => Post.objects.all()[offset:offset+limit]

# 3. Update
# post = Post.objects.get(pk=1)
# post.title = 'yo-5'
# post.save() #실제 DB에 저장

# 4. Delete
# post = Post.objects.get(pk=1)
# post.delete()
# 한줄로
# Post.objects.get(pk=1).delete()