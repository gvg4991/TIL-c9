from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content',) #admin에서 파일명을 제목과 컨텐츠로 보이도록 함

# Register your models here.
admin.site.register(Post, PostAdmin)