from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('docs/', get_swagger_view(title='API Docs')), #swagger는 제목을 붙여줘야됨 
    path('musics/', views.music_list),
    path('musics/<int:music_id>/', views.music_detail),
    path('musics/<int:music_id>/comments/', views.comment_create),
    path('musics/<int:music_id>/comments/<int:comment_id>/',views.comment_update_and_delete),
    path('artists/',views.artist_list),
    path('artists/<int:artist_id>/', views.artist_detail),
    ]