from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #장고에서 만들어 둔 폼을 가지고 옴
from django.contrib.auth import login as auth_login # as를 통해 함수 이름을 변경(알아보기 쉬우려고)
from django.contrib.auth import logout as auth_logout

# Create your views here.

# 유저 만들기
def signup(request):
    if request.user.is_authenticated: #유저가 로그인이 되어 있다면(현재 로그인된 유저 정보 가지고옴)
        return redirect('posts:list')    

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form':form})

# Session create
# 존재하는 유저인지 검증
def login(request):
    if request.user.is_authenticated: #유저가 로그인이 되어 있다면(현재 로그인된 유저 정보 가지고옴)
        return redirect('posts:list')
    
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) #세션을 크리에이트해줌
            return redirect(request.GET.get('next') or 'posts:list') #posts의 list로 리다이렉트 해줌
    else:
        form = AuthenticationForm()
    
    #request.GET.get('next') => /posts/new/ (url에 넥스트로 얻을 경우 new로 보내줌)
    return render(request, 'login.html', {'form':form})
    

def logout(request):
    auth_logout(request)
    return redirect('posts:list')