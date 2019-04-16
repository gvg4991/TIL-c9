from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, ProfileForm, CustomUserCreationForm #우리가 폼즈.py에 만든 폼을 가지고 와서 적용하겠다
from .models import Profile


# Create your views here.
def signup(request):
    if request.user.is_authenticated: #로그인이 되어있는 상태라면
        return redirect('posts:list')
    
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST) #리퀘스트 값을 받아와서 폼에 저장을함
        if signup_form.is_valid(): #아이디가 너무 쉬운지 검증
            user = signup_form.save() #통과되면 저장
            Profile.objects.create(user=user)
            auth_login(request, user) #로그인할 윶의 객체를 넣어줌
            return redirect('posts:list') #로그인페이지로 돌려보냄(지금은 로그인 페이지 없어서 리스트페이지로 보냄)
    else:
        signup_form = CustomUserCreationForm()
    return render(request,'accounts/signup.html', {'signup_form':signup_form})
    
    
# from django.contrib.auth import login as auth_login
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
    
    
# from django.contrib.auth import logout as auth_logout
def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    

# from django.contrib.auth import get_user_model
def people(request, username):
    #get_user_model -> User
    people = get_object_or_404(get_user_model(), username=username) #앞의 유저네임은 컬럼, 뒤에 유저네임은 주소로 부터 받은것
    return render(request, 'accounts/people.html', {'people':people})
    
    
# USER edit(회원정보 수정) - user CRUD 중 U
# from django.contrib.auth.decorators import login_required
@login_required #로그인 했을때만 가능
def update(request):
    # 포스트폼을 만들어서 생성하고 수정하고 했음
    # 장고에서 유저를 업데이트 하는 폼을 가지고있음 (UserChangeForm을 임포트)
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('people',request.user.username) #people페이지로 이동
    else: #겟방식일때
        # user_change_form = UserChangeForm(instance=request.user) #(인스턴스가 현재 유저인)폼의 정보를 변수에 저장 - 모든 정보를 수정할 수 있는 폼
        user_change_form = CustomUserChangeForm(instance=request.user)
    return render(request,'accounts/update.html',{'user_change_form':user_change_form}) #새로운 페이지(어카운츠의 업데이트html)를 보여줌
    
    
# 회원 탈퇴 - suer CRUD 중 D
@login_required
def delete(request):
    if request.method == 'POST': #포스트 방식이라면 삭제하고 리스트페이지로 이동
        request.user.delete()
        return redirect('posts:list')
    return render(request, 'accounts/delete.html')
    
    
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash
@login_required
def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request,user) #비번 바꾸고 로그인 상태 유지(비밀번호가 변경된 유저의 정보를 가지고 와서 세션 비밀번호에 넣는다)
            return redirect('people',request.user.username)
    else:
        password_change_form = PasswordChangeForm(request.user) #어떠한 유저의 정보를 넣을건지만 작성하면됨('instance='' 필요없음)
    return render(request, 'accounts/password.html',{'password_change_form':password_change_form})
    
    
# from .forms import ProfileForm
def profile_update(request):
    profile = request.user.profile
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('people',request.user.username)
    else:
        profile_form = ProfileForm(instance = profile)
    return render(request, 'accounts/profile_update.html', {'profile_form':profile_form,}) #profile_form을 사용하기위해 딕셔너리 형태로 넣어줌
    
    
    
# 팔로우
def follow(request, user_id):
    people = get_object_or_404(get_user_model(),id=user_id) #특정한 모델에서 id값이 특정 user에 저장
        
    if request.user in people.followers.all():    
    # 2.people을 언팔하기
        people.followers.remove(request.user)
    else:
    # 1.그 사람의 팔로워에 자신을 추가
        people.followers.add(request.user) 
        
    return redirect('people',people.username)