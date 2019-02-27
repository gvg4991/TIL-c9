from django.shortcuts import render, redirect
from .models import Post, Comment #현재 폴더에 있는 모델스라는 파일에서 Post클래스를 이용한다. 

# Create your views here.

def new(request):
    if request.method == 'POST':
        #create
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        post = Post(title=title, content=content, image=image)
        post.save() #post인스턴스에 저장
    
        return redirect('posts:detail',post.pk)
    
    else:
        #new
        return render(request,'new.html')

# def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # image = request.FILES.get('image')
        
    # post = Post(title=title, content=content, image=image)   #models의 Post클래스에 title과 content를 넣고 인스턴스 생성
    # post.save() #post인스턴스에 저장
    
    # return redirect('posts:detail',post.pk)    #posts/detail/ url에 추가적인 파라메타<int:post_id>를 ,로 구분하여 작성

    
def index(request): # 모든 포스트를 보여줌
    posts = Post.objects.all() #Post클래스의 모든 객체들을 posts(앱이름아님)에 저장
    return render(request, 'index.html', {'posts':posts})
    
def detail(request):

        
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        #update
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        
        return redirect('posts:detail',post.pk)
    else:
        # post = Post.objects.get(pk=post_id)
        # edit
        return render(request,'edit.html', {'post':post})
    
# def update(request, post_id):
#     #수정하는 코드
#     post = Post.objects.get(pk=post_id)
#     post.title = request.POST.get('title')
#     post.content = request.POST.get('content')
#     post.save() #실제로 멤버변수에 방영하기
#     return redirect('posts:detail',post.pk)
    
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