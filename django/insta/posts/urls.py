from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.list, name='list'),
    path('create/', views.create, name='create'), #주소에 대한이름을 name으로 지정
    path('<int:post_id>/update/', views.update, name = 'update'),
    path('<int:post_id>/delete/', views.delete, name='delete'), #앞쪽에는 변수에 들어오는 인풋 <타입:변수명>
    ]