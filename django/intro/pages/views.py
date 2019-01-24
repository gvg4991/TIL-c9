from django.shortcuts import render
import random

# Create your views here.
def index(request): #request 요청에서 받아옴
    return render(request, 'index.html')

# Template variable
def dinner(request):
    menu=['흰쌀밥','뜨끈한국','각종반찬']
    pick=random.choice(menu)
    return render(request, 'dinner.html', {'dinner':pick})
    
# Variable routing
def hello(request, name): #이름을 주소로 부터 받음
    return render(request,'hello.html',{'name':name})
    
# Study hard
member=[]
def ediya(request, who):
    member=who.split()
    money=random.choice(member)
    member.remove(money)
    no_drink=random.choice(member)
    return render(request, 'ediya.html', {'money':money,'no_drink':no_drink})

# From tag (내부에서 보내기)
def throw(request):
    return render(request, 'throw.html')
    
def catch(request):
    message = request.GET.get('message')
    return render(request, 'catch.html', {'message': message})
    
# Form 외부로 요청
def naver(request):
    return render(request, 'naver.html')
    
# Bootstrap
def bootstrap(request):
    return render(request,'bootstrap.html')