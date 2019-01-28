from django.shortcuts import render
from .models import Post #현재 폴더에 있는 모델스라는 파일에서 Post클래스를 이용한다. 

# Create your views here.

def new(request):
    return render(request,'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # DB INSERT
    post = Post(title=title, content=content)
    post.save()
    
    return render(request, 'create.html')
    
def index(request): #인덱스에 작성된 new와 create를 게시판과 같이 작성시킴
    # All post
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts':posts})