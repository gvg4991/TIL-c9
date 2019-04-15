from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #로그인 데코레이터
from django.views.decorators.http import require_POST, require_http_methods
from .forms import PostForm, CommentForm, ImageFormSet #폼을 불러옴
from .models import Post, Comment
from django.db import transaction


# Create your views here.


def list(request):
    posts = Post.objects.order_by('-id').all()
    comment_form = CommentForm()
    return render(request,'posts/list.html', {'posts':posts, 'comment_form':comment_form}) #render일때, 변수 넘겨주기!


@login_required #이 함수를 실행하려면 로그인이 되어있어야한다(데코레이터의 파라메터로 밑에있는 함수를 받음)
def create(request): #첫번째는 request를 인자로 받음
    if request.method == 'POST':
        post_form = PostForm(data=request.POST) #뒤에 POST, FILES는 대문자로 받기 (content만 올라감)
        image_formset = ImageFormSet(data=request.POST, files=request.FILES) #(이미지만 올라감)
        if post_form.is_valid() and image_formset.is_valid(): #둘다 유효한가
            # 작성자명 입력
            post = post_form.save(commit=False) #데이터베이스에 저장할때 객체를 post라는 변수에 담음
            post.user = request.user #포스트라는 객체의 유저에 현재 유저를 입력
            
            
            # from django.db import transaction
            with transaction.atomic(): #순서대로 진행할 수 있도록 보장해줌. (post가 생긴 다음에 이미지를 만들라!)
                # 1. 포스트가 먼저 생성돼야됨(그래야 아이디값이 생김) 
                post.save() #실제 데이터베이스에 저장
                # 2. 이미지를 만듬
                image_formset.instance = post #부모모델의 인스턴스를 넣어줌(유저 정보를 넣어줌) - 어렴노ㅠㅠ
                image_formset.save()
            
            
            return redirect('posts:list')
    else:
        post_form = PostForm()
        image_formset = ImageFormSet() #폼형식 데이터를 넣어줌
    return render(request, 'posts/form.html', {'post_form':post_form, 'image_formset':image_formset,}) #여러개 app을 만들 경우, posts라는 앱이름으로 폴더명 경로를 넣어줌
    
    
    
@login_required
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if post.user != request.user:
        return redirect('posts:list')
    
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post) #instance=post가 create함수와 다른 부분!
        image_formset = ImageFormSet(request.POST, request.FILES, instance=post)
        if post_form.is_valid() and image_formset.is_valid():
            post_form.save() #forms에서 설정해 줘서 바로 post에 저장할 수 있음
            image_formset.save()
            return redirect('posts:list')
    else: #주소창에 입력을 받았을 경우!
        post_form = PostForm(instance=post)
        image_formset = ImageFormSet(instance=post) #post가 가지고 있는 이미지를 가지고 만듬 
    return render(request, 'posts/form.html', {'post_form':post_form, 'image_formset':image_formset,})
    
    
    
@login_required
def delete(request, post_id): #어떤 게시물을 삭제할지 받아와야함(주소를통해 받아올 포스트의 아이디)
    # post = Post.objects.get(id=post_id) #id값이 포스트 카드인 데이터를 불러옴 (pk프라이머리키보다 id가 많이쓰임)
    post = get_object_or_404(Post, id=post_id) #메소드의 반환값이 포스트가 됨(게시물이 없으면 404에러 발생)
    
    if post.user != request.user:
        return redirect('posts:list')
        
    post.delete()
    
    # post.delete()
    # return redirect('posts:list')
    
    return redirect('posts:list')
    
    

@login_required #가장위에있는 데코레이터부터 확인
@require_POST
def comment_create(request, post_id): #포스트의 정보를 가지고와서 댓글을 쓰기때문에 아이디 받아줌
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        comment.save()
    return redirect('posts:list') #댓글을 생성하는 페이지가 따로있는게 아니고 행동만 정의하면 돼서
    

@require_http_methods(['GET','POST'])
def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return redirect('posts:list')
        
    comment.delete()
    return redirect('posts:list')
    
    

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