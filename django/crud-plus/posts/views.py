from django.shortcuts import render, redirect
from .models import Post, Comment #현재 폴더에 있는 모델스라는 파일에서 Post클래스를 이용한다. 

# Create your views here.

def new(request):
    return render(request,'new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # DB INSERT
    post = Post(title=title, content=content)   #models의 Post클래스에 title과 content를 넣고 인스턴스 생성
    post.save() #post인스턴스에 저장
    
    return redirect('posts:detail',post.pk)    #posts/detail/ url에 추가적인 파라메타<int:post_id>를 ,로 구분하여 작성
    
def index(request): #인덱스에 작성된 new와 create를 게시판과 같이 작성시킴
    # All post
    posts = Post.objects.all()  #Post클래스의 객체를 모두 posts에 저장
    
    return render(request, 'index.html', {'posts':posts})   #index.html에 posts 입력
    
def detail(request, post_id):
    post = Post.objects.get(pk=post_id) #포스트의 아이디값을 얻어 객체를 불러와서 post에 저장
    return render(request, 'detail.html', {'post':post})    #저장된 post를 detail의 post에 입력
    
def delete(request, post_id):
    #삭제하는 코드
    post = Post.objects.get(pk=post_id) #게시글 하나 불러오기! id값을 
    post.delete()
    return redirect('posts:list') #posts에서 삭제가 이뤄짐
    
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request,'edit.html', {'post':post})
    
def update(request, post_id):
    #수정하는 코드
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save() #실제로 멤버변수에 방영하기
    return redirect('posts:detail',post.pk)
    
def comments_create(request, post_id):
    # 댓글 달 게시물c
    post = Post.objects.get(pk=post_id)
    # form에서 넘어온 댓글 내용
    content = request.POST.get('content')
    # 댓글 생성 및 저장
    comment = Comment(post=post, content=content)
    comment.save()
    return redirect('posts:detail',post.pk)     #redirect에서 url명으로 들어가는 형태
    
def comments_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('posts:detail', post_id)
    
# # 외부로 보내는 redirect
# def naver(request, q):
#     return redirect(f'https://search.naver.com/search.naver?query={q}')
    
# def github(request, username):
#     return redirect(f'https://github.com/{username}')