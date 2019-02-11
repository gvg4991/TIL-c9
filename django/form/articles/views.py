from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleModelForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST) #request.POST를 통해 
        if form.is_valid():
            article = form.save()
            # title = form.cleaned_data.get('title') #form의 검증을 통과한 데이터들을 넣음
            # content = form.cleaned_data.get('content')
            # # article = Article(title=title, content=content)
            # # article.save()
            # article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleModelForm() #인스턴스를 만들어서 크리에이트에 넘겨줌
        
    return render(request,'form.html', {'form':form})
        

def detail(request, article_id): # article_id를 받아야 됨
    article = Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'article':article})
    
    
def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    #크리에이트 복붙
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article) #instance=article로 정보 수정
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleModelForm(instance=article) #()안의 내용을 작성하여 수정하기 전 기존 정보를 세팅해줌
        
    return render(request,'form.html', {'form':form})