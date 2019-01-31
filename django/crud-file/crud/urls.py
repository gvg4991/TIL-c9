"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #urls를 다른 파일에서 가지고 올 경우 include
from django.conf.urls.static import static
from django.conf import settings
from posts import views

urlpatterns = [
    path('posts/', include('posts.urls')), #urls를 다른 파일에서 설정하여 가지고 옴
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
#사용자가 올리는 파일이름은 정확히 알수가 없음. 어떤 이미지를 올리든지 받아들일 수 있음.