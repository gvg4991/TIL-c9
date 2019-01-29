from django.shortcuts import render, redirect
from .models import Save

# Create your views here.
def new(request):
    return render(request,'new.html')

def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    
    saves = Save(name=name, email=email, birthday=birthday, age=age)
    saves.save()
    
    return redirect(f'/{saves.pk}')
    
def index(request):
    save = Save.objects.all()
    return render(request, 'index.html', {'save':save})
    
def detail(request, saves_id):
    saves = Save.objects.get(pk=saves_id) #포스트의 아이디값을 얻어 객체를 불러와서 post에 저장
    return render(request, 'detail.html', {'saves':saves})    #저장된 post를 detail의 post에 입력
    
def delete(request, saves_id):
    #삭제하는 코드
    saves = Save.objects.get(pk=saves_id) #게시글 하나 불러오기!
    saves.delete()
    return redirect('/') #posts에서 삭제가 이뤄짐
    
def edit(request, saves_id):
    saves = Save.objects.get(pk=saves_id)
    return render(request,'edit.html', {'saves':saves})
    
def update(request, saves_id):
    #수정하는 코드
    saves = Save.objects.get(pk=saves_id)
    saves.name = request.POST.get('name')
    saves.email = request.POST.get('email')
    saves.birthday = request.POST.get('birthday')
    saves.age = request.POST.get('age')
    saves.save() #실제로 멤버변수에 방영하기
    return redirect(f'/{saves_id}/')