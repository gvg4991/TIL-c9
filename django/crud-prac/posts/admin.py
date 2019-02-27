from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','created_at','updated_at',) #admin에서 파일명을 제목과 컨텐츠로 보이도록 함

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)