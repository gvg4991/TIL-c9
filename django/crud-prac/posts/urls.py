from django.urls import path
from . import views

app_name = 'posts' # 이 url의 주소는 posts다

urlpatterns = [
    # path('naver/<str:q>/',views.naver),
    # path('github/<str:username>',views.github),
    
    path('',views.index, name='index'),
    # path('create/', views.create, name='create'),
    path('new/', views.new, name='new'), #url에 이름을 지정해줌으로써 주소창 new/를 write/로 바꿔도 문제없이 실행됨 (GET(new), POST(create))
 
    path('<int:post_id>/edit/', views.edit, name='edit'), #(GET(edit), POST(update))
    # path('<int:post_id>/update/', views.update, name='update'), 
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'), #뷰즈에서 만든 comments_create함수 이용
    path('<int:post_id>/comments/<int:comment_id>/delete/',views.comments_delete, name='comments_delete'),
]
