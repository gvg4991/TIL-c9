from django.contrib import admin
from .models import Save

class SaveAdmin(admin.ModelAdmin):
    list_display = ('name','email','birthday','age',) #admin에서 파일명을 제목과 컨텐츠로 보이도록 함

# Register your models here.
admin.site.register(Save, SaveAdmin)
