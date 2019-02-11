from django import forms
from .models import Article #모델즈의 클래스를 정의함

class ArticleForm(forms.Form):
    title = forms.CharField(label='제목') # forms.에서 가지고 온 캐릭터필드는 ()안에 범위지정 필수 아님.
    content = forms.CharField(label='내용', widget=forms.Textarea(attrs={
        'row': 5,
        'cols': 50,
        'placeholder':'내용을 입력하세요.',
    }))
    
class ArticleModelForm(forms.ModelForm):
    class Meta: #아티클모델폼 클래스의 정보를 가지고 있음(데이터를 설명하는 데이터)
        model = Article
        fields = ['title','content']