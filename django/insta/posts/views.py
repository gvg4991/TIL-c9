from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post


# Create your views here.


def list(request):
    posts = Post.objects.all()
    return render(request,'posts/list.html', {'posts':posts})



def create(request): #첫번째는 request를 인자로 받음
    if request.method == 'POST':
        post_form = PostForm(data=request.POST, files=request.FILES) #뒤에 POST, FILES는 대문자로 받기
        if post_form.is_valid():
            post_form.save() #forms에서 설정해 줘서 바로 post에 저장할 수 있음
            return redirect('posts:list')
    else:
        post_form = PostForm()
    return render(request, 'posts/create.html', {'post_form':post_form}) #여러개 app을 만들 경우, posts라는 앱이름으로 폴더명 경로를 넣어줌
    
    
    
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post) #instance=post가 create함수와 다른 부분!
        if post_form.is_valid():
            post_form.save() #forms에서 설정해 줘서 바로 post에 저장할 수 있음
            return redirect('posts:list')
    else: #주소창에 입력을 받았을 경우!
        post_form = PostForm(instance=post)
    return render(request, 'posts/create.html', {'post_form':post_form})
    
    

def delete(request, post_id): #어떤 게시물을 삭제할지 받아와야함(주소를통해 받아올 포스트의 아이디)
    # post = Post.objects.get(id=post_id) #id값이 포스트 카드인 데이터를 불러옴 (pk프라이머리키보다 id가 많이쓰임)
    post = get_object_or_404(Post, id=post_id) #메소드의 반환값이 포스트가 됨(게시물이 없으면 404에러 발생)
    post.delete()
    return redirect('posts:list')