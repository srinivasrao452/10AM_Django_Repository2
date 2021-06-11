
from django.contrib import admin

from OneToOne_App.models import Student,Cource

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','sno','sname','marks']

class CourceAdmin(admin.ModelAdmin):
    list_display = ['id','cno','cname','cfee','student_id']

admin.site.register(Student,StudentAdmin)
admin.site.register(Cource,CourceAdmin)


