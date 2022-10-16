from django.contrib import admin

from student.models import studentStudentModel, studentMarksModel, studentSubjectsModel

# Register your models here.

class studentClientStudentAdmin(admin.ModelAdmin):
    list_display = ['']
admin.site.register(studentStudentModel)
admin.site.register(studentSubjectsModel)
admin.site.register(studentMarksModel)
