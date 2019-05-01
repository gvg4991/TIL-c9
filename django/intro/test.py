## form을 이용한 CRUD
# models.py
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Movie(models.Model):   #Post 클래스를 생성
    title = models.CharField(max_length=100)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
class Score(models.Model):
    content = models.CharField(max_length=100)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    

    


#forms.py
from django import forms
from .models import Score, Movie

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['content','score',]
        
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'




#views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Score, Genre
from .forms import ScoreForm, MovieForm

# Create your views here.
def list(request): #인덱스에 작성된 new와 create를 게시판과 같이 작성시킴
    movies = Movie.objects.all()  #Post클래스의 객체를 모두 posts에 저장
    return render(request, 'list.html', {'movies':movies})   #index.html에 posts 입력
    
def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id) #포스트의 아이디값을 얻어 객체를 불러와서 post에 저장
    score_form = ScoreForm()
    return render(request, 'detail.html', {'movie':movie, 'score_form':score_form})    #저장된 post를 detail의 post에 입력

def new(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie = movie_form.save(commit=False)
            movie.save()
            return redirect('movies:detail',movie.id)
    else:
        movie_form = MovieForm()
    return render(request, 'form.html', {'movie_form':movie_form})
    
def edit(request, movie_id):
    movie = get_object_or_404(Movie,id=movie_id)
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie = movie_form.save(commit=False)
            movie.save()
            return redirect('movies:detail',movie.id)
    else:
        movie_form = MovieForm(instance=movie)
    return render(request, 'form.html', {'movie_form':movie_form})

def delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id) #게시글 하나 불러오기! id값을 
    movie.delete()
    return redirect('movies:list') #posts에서 삭제가 이뤄짐
    
def score_create(request, movie_id): #포스트의 정보를 가지고와서 댓글을 쓰기때문에 아이디 받아줌
    score_form = ScoreForm(request.POST)
    if score_form.is_valid():
        score = score_form.save(commit=False)
        score.movie_id = movie_id
        score.save()
    return redirect('movies:detail',movie_id) #댓글을 생성하는 페이지가 따로있는게 아니고 행동만 정의하면 돼서
    
def score_delete(request, movie_id, score_id):
    score = get_object_or_404(Score, id=score_id)
    score.delete()
    return redirect('movies:detail',movie_id)
    
    
    
    
    
#urls.py
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('',views.list, name='list'),
    path('<int:movie_id>/',views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:movie_id>/edit/', views.edit, name='edit'),
    path('<int:movie_id>/delete/', views.delete, name='delete'),
    path('<int:movie_id>/scores/new/',views.score_create, name='score_create'), #댓글 url
    path('<int:movie_id>/scores/<int:score_id>/delete/',views.score_delete, name='score_delete'),
    ]
    
    
    
    
    
    
#html
{% extends 'base.html' %}

{% block container %}

<img src="{{movie.poster_url}}"></img>
<h2>Title : {{ movie.title }}</h2>
<p>Genre : {{ movie.genre.name }}</p>
<p>Audience : {{ movie.audience }}</p>
<p>Poster_url : {{ movie.poster_url }}</p>
<p>Description : {{ movie.description }}</p>

<form action="{% url 'movies:delete' movie.id %}" method='post'> <!--post요청으로 보냄-->
    {% csrf_token %}
    <a href="/movies/">list</a>
    <a href="/movies/{{movie.id}}/edit/">Edit</a>
    <input type="submit" value="삭제"/>
</form>

<br>
<hr>
<!--평점-->
{% for score in movie.score_set.all %}
<!--{{ score.content }} {{ score.score }}-->
<form action="{% url 'movies:score_delete' movie.id score.id %}" method="POST">
    {% csrf_token %}
    content : {{ score.content }} (Score : {{ score.score }})
    <input type="submit" value="삭제"/>
</form>
{% endfor %}

<form action="{% url 'movies:score_create' movie.id %}" method = "POST">
    {% csrf_token %}
    {{ score_form }}
    <input type="submit" value="등록"/>
</form>

{% endblock %}






#-------------------------------------------------------------------------------------------------------------------------
## accounts
# base.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {% if user.is_authenticated %}
        <h1>
            Yo! {{user.username}}
            <a href="{% url 'accounts:logout' %}">로그아웃</a>
        </h1>
    {% else %}
        <h1>
            <a href="{% url 'accounts:login' %}">로그인</a>
            <a href="{% url 'accounts:signup' %}">회원가입</a>
        </h1>
    {% endif %}
    
    {% block container %} 
    {% endblock %}
</body>
</html>






#views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm #, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import get_user_model
from itertools import chain
from .models import User
from .forms import UserCustomCreationForm

# Create your views here.
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated: # 로그인 되어있는 상태이면
        return redirect('movies:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user) # 정보를 가지고 자동로그인
            return redirect('movies:list')
    else:
        user_form = UserCustomCreationForm()
    context = {'form': user_form}
    return render(request, 'accounts/forms.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST) # 포스트 형식으로 받은 정보를 폼 형식으로 지정해준다
        if login_form.is_valid():
            auth_login(request, login_form.get_user()) # 현재 유저의 정보로 로그인을 한다
            return redirect('movies:list')
    else:
        login_form = AuthenticationForm()
    context = {'form': login_form}
    return render(request, 'accounts/forms.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:list')
    
    
def list(requset):
    users = User.objects.all()
    return render(requset, 'accounts/list.html', {'users':users} )
    
    
def detail(request, user_pk):
    people = User.objects.get(pk=user_pk)
    
    total=[]
    for friends in people.followings.all():
        comment=friends.score_set.all().order_by('-score').first()
        total.append(comment)
        
    return render(request, 'accounts/detail.html', {'people':people,'total':total})

    

@login_required
def follow(request, user_pk):
    people = get_object_or_404(get_user_model(),id=user_pk)
    
    if request.user in people.followers.all():    
    # 2.people을 언팔하기
        people.followers.remove(request.user)
    else:
    # 1.그 사람의 팔로워에 자신을 추가
        people.followers.add(request.user) 
        
    return redirect('accounts:detail',people.id)
  







# urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('',views.list, name='list'),
    path('<int:user_pk>/', views.detail, name='detail'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]








#html(login)
{% extends 'base.html' %}

{% block container %}
<h1>로그인</h1>

<form method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit"/>
</form>

{% endblock %}



#html(sign up)
{% extends 'base.html' %}

{% block container %}

<h1>회원가입</h1>

<form method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit"/>
</form>

{% endblock %}





#-------------------------------------------------------------------------------
## like
# views.py
@login_required
def like(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    if request.user in post.like_users.all():
        #2.조아연 취소
        post.like_users.remove(request.user)
    else:
        #1.조아연
        post.like_users.add(request.user) #현재 로그인된 유저==request.user
    return redirect('posts:list')
    
    
    
    
    
    
# models.py
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #외부키를 가지고옴, CASCADE(어떤게 삭제되면 그의 옵션들이 같이 삭제됨)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')





# html
 <div class='card-body'>
    <a href="{% url 'posts:like' post.id %}">
      {% if user in post.like_users.all %}
        <i class="fas fa-heart"></i>
      {% else %}
        <i class='far fa-heart'></i>
      {% endif %}
    </a>
  <p class="card-text">
    {{ post.like_users.count }}명이 좋아합니다.
  </p>
  </div>
  <div class="card-body">
    <p class="card-text">{{ post.content }}</p>
    {% if post.user == user %} <!--작성자와 유저가 같을때만 버튼생성-->
    <a href="{% url 'posts:update' post.id %}" class="btn btn-info">Edit</a>
    <a href="{% url 'posts:delete' post.id %}" class="btn btn-warning">Delete</a>
    <!--post의 아이디를 받음-->
    {% endif %}
  </div>
  <div class="card-body">
    {% for comment in post.comment_set.all %}
      <div class="card-text">
        <strong>{{ comment.user.username }}</strong> {{ comment.content }}
        {% if comment.user == user %} <!--댓글 쓴 유저와 현재 로그인 유저가 같다면-->
        <a href="{%url 'posts:comment_delete' post.id comment.id %}">삭제</a>
        {% endif %}
      </div>
    {% empty %}
      <div class='card-text'>댓글이 없습니다.</div>
    {% endfor %}
  </div>
  {% if user.is_authenticated %}
  <form action="{% url 'posts:comment_create' post.id %}" method = "POST">
    {% csrf_token %}
    <div class="input-group">
      {{ comment_form }}
      <div class="input-group-prepend">
        <input type="submit" value="Submit" class='btn btn-info'/>
      </div>
    </div>
  </form>
  {% endif %}
</div>