from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content','image',]
        
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'댓글을 작성하세요'})) #클래스 여러가 쓰고싶으면 클래스 ''안에 띄어쓰기하고 적기
    
    class Meta:
        model = Comment
        fields = ['content',]