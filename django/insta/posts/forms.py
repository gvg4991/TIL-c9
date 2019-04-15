from django import forms
from .models import Post, Comment, Image #클래스를 임포트 해줘야됨

class PostForm(forms.ModelForm):
    class Meta:
        model = Post #포스트를 모델로 받음
        fields = ['content',]
        
        
class ImageForm(forms.ModelForm): #이미지라는 모델에 작성을하기위해 정의하는 폼
    class Meta:
        model = Image
        fields = ['file',] #하나의 이미지 폼의 파일을 필드에 보여줌
        
        
ImageFormSet = forms.inlineformset_factory(Post, Image, form=ImageForm, extra=3) #.save를했을때 생성되는 이미지
#이미지를 들고있는 모델을 넣어줘야됨, 이미지, 이미지를 넣을 수 있는 폼을 넣어줌, 이미지를 몇개까지 넣을 수 있는 정의(이미지 폼이 세개가 들어간다고 생각하면됨)

        
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'댓글을 작성하세요'})) #클래스 여러가 쓰고싶으면 클래스 ''안에 띄어쓰기하고 적기
    
    class Meta:
        model = Comment
        fields = ['content',]