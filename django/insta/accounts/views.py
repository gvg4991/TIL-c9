from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.user.is_authenticated: #로그인이 되어있는 상태라면
        return redirect('posts:list')
    
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST) #리퀘스트 값을 받아와서 폼에 저장을함
        if signup_form.is_valid(): #아이디가 너무 쉬운지 검증
            user = signup_form.save() #통과되면 저장
            auth_login(request, user) #로그인할 윶의 객체를 넣어줌
            return redirect('posts:list') #로그인페이지로 돌려보냄(지금은 로그인 페이지 없어서 리스트페이지로 보냄)
    else:
        signup_form = UserCreationForm()
    return render(request,'accounts/signup.html', {'signup_form':signup_form})
    
    
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid(): #실제로 존재하는 유저라면
            auth_login(request,login_form.get_user()) #실제로 로그인해주는 기능
            return redirect(request.GET.get('next') or 'posts:list') #get값에 next가 있으면 앞에거 이용해서 바로 이전 작업페이지(create)로 이동, 없으면 뒤에거 이용
    else:
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form':login_form})
    
    
def logout(request):
    auth_logout(request)
    return redirect('posts:list')