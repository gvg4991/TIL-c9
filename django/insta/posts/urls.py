from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.list, name='list'),
    path('explore/',views.explore,name='explore'),
    path('create/', views.create, name='create'), #주소에 대한이름을 name으로 지정
    path('<int:post_id>/update/', views.update, name = 'update'),
    path('<int:post_id>/delete/', views.delete, name='delete'), #앞쪽에는 변수에 들어오는 인풋 <타입:변수명>
    path('<int:post_id>/comments/create/',views.comment_create, name='comment_create'), #댓글 url
    path('<int:post_id>/comments/<int:comment_id>/delete/',views.comment_delete, name='comment_delete'),
    path('<int:post_id>/like/',views.like,name='like'),
    ]