from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save

from practice.uitls import parcticestudentMainGradeEnumTypes
from school_core.uitls import slug_pre_save_receiver

User = get_user_model()

"""
title 
discription
marks-gain--enni
marks-------100 ki
student-fk-
"""
class PracticeSubjectModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    marks=models.IntegerField(default=100)
    marks_gain=models.IntegerField(default=0)
    student=models.ForeignKey(User,on_delete=models.CASCADE,related_name="PracticeSubjectModel_student")

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.student)

pre_save.connect(slug_pre_save_receiver, sender=PracticeSubjectModel)


"""
student ---oto
total marks
grade
subjects ---mtm


"""
class PracticeStudentMainModel(models.Model):
    student=models.OneToOneField(User,on_delete=models.CASCADE,related_name="PracticeStudentMainModel_student")
    total_marks=models.IntegerField(default=0)
    grade = models.CharField(max_length=20, choices=parcticestudentMainGradeEnumTypes.choices(), null=True, blank=True)
    subjects=models.ManyToManyField(PracticeSubjectModel,related_name="PracticeStudentMainModel_subjects")

    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.student)


pre_save.connect(slug_pre_save_receiver, sender=PracticeStudentMainModel)
