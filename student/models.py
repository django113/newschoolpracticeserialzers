from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum
from django.db.models.signals import pre_save, post_save, post_delete

from school_core.uitls import slug_pre_save_receiver
from django.utils.translation import gettext_lazy as _

from student.signals import subject_code_unique_code_generator
from student.uitls import studentGradeEnumTypes

User = get_user_model()

"""
student = required
address = required
date_created = required
slug = required
"""


# <editor-fold desc="WHEN USER IS CREATED THEN STUDENT MODEL USER ALSO CREATED">
def student_post_save_receiver(sender, created, instance, *args, **kwargs):
    if created:
        studentStudentModel.objects.create(student=instance)
# </editor-fold>


# <editor-fold desc="STUDENT SUBJECT CREATED THEN STUDENT AND STUDENT MARKS UPDATED OR CREATED ">
def subject_post_save_receiver(sender, created, instance, *args, **kwargs):
    if created:
        print(instance.student, "====================")
        instance_marks = studentSubjectsModel.objects.all().filter(student_id=instance.student.id).aggregate(
            Sum('score_marks'))
        marks = studentSubjectsModel.objects.all().filter(student=instance.student).values_list('marks', flat=True)

        print(sum(marks), 'max marks')
        print('scored marks', instance_marks)

        print('instance_marks', list(instance_marks.values())[0])

        print("instance subjects", instance.subject)
        try:
            student = studentStudentModel.objects.get(student=instance.student)
        except:
            student = studentStudentModel.objects.create(student=instance.student)

        print("student=========", student)

        student_mark = studentMarksModel.objects.filter(student=student)
        if student_mark.exists():
            instnace_student_marks = student_mark
            print("instance student marks", instnace_student_marks)

            try:
                student_Mark_subject = studentMarksModel.objects.get(student=student)
            except:
                student_Mark_subject = student_mark

            student_Mark_subject.total_marks = list(instance_marks.values())[0]
            student_Mark_subject.marks = sum(marks)

            print(student_Mark_subject.total_marks, '================total marks=================', sum(marks))

            student_grade = (student_Mark_subject.total_marks / student_Mark_subject.marks) * 100
            print("percentage=====1========", student_grade)
            if student_grade >= 100:
                student_Mark_subject.grade = "A"
            elif student_grade >= 80:
                student_Mark_subject.grade = "B"
            elif student_grade >= 60:
                student_Mark_subject.grade = "C"
            elif student_grade >= 40:
                student_Mark_subject.grade = "D"
            elif student_grade >= 35:
                student_Mark_subject.grade = "F"
            else:
                student_Mark_subject.grade = ''
            student_Mark_subject.save()
            student_Mark_subject.subjects.add(instance.id)


        else:
            try:
                student_Mark_subject = studentMarksModel.objects.get(student=student)
            except:
                student_Mark_subject = studentMarksModel.objects.create(student=student)

            student_Mark_subject.total_marks = list(instance_marks.values())[0]
            student_Mark_subject.marks = sum(marks)

            print(student_Mark_subject.total_marks, '================total marks=======2======', sum(marks))
            student_grade = (student_Mark_subject.total_marks / student_Mark_subject.marks) * 100
            print("percentage======2=======", student_grade)
            if student_grade >= 100:
                student_Mark_subject.grade = "A"
            elif student_grade >= 80:
                student_Mark_subject.grade = "B"
            elif student_grade >= 60:
                student_Mark_subject.grade = "C"
            elif student_grade >= 40:
                student_Mark_subject.grade = "D"
            elif student_grade >= 35:
                student_Mark_subject.grade = "F"
            else:
                student_Mark_subject.grade = ''
            student_Mark_subject.save()

            student_Mark_subject.subjects.add(instance.id)
    if instance:
        print(instance.student, "====================")
        instance_marks = studentSubjectsModel.objects.all().filter(student_id=instance.student.id).aggregate(
            Sum('score_marks'))
        marks = studentSubjectsModel.objects.all().filter(student=instance.student).values_list('marks', flat=True)

        print('instance_marks', list(instance_marks.values())[0])

        print("instance subjects", instance.subject)
        try:
            student = studentStudentModel.objects.get(student=instance.student)
        except:
            student = studentStudentModel.objects.create(student=instance.student)

        print("student=========", student)

        student_mark = studentMarksModel.objects.filter(student=student)
        if student_mark.exists():
            instnace_student_marks = student_mark
            print("instance student marks", instnace_student_marks)

            try:
                student_Mark_subject = studentMarksModel.objects.get(student=student)
            except:
                student_Mark_subject = student_mark

            student_Mark_subject.total_marks = list(instance_marks.values())[0]
            student_Mark_subject.marks = sum(marks)

            print(student_Mark_subject.total_marks, '================total marks=============',
                  list(instance_marks.values())[0], "============", sum(marks))

            student_grade = (student_Mark_subject.total_marks / student_Mark_subject.marks) * 100
            print("percentage======3=======", student_grade)
            if student_grade >= 100:
                student_Mark_subject.grade = "A"
            elif student_grade >= 80:
                student_Mark_subject.grade = "B"
            elif student_grade >= 60:
                student_Mark_subject.grade = "C"
            elif student_grade >= 40:
                student_Mark_subject.grade = "D"
            elif student_grade >= 35:
                student_Mark_subject.grade = "F"
            else:
                student_Mark_subject.grade = ''
            student_Mark_subject.save()
            student_Mark_subject.subjects.add(instance.id)


        else:
            try:
                student_Mark_subject = studentMarksModel.objects.get(student=student)
            except:
                student_Mark_subject = studentMarksModel.objects.create(student=student)

            student_Mark_subject.total_marks = list(instance_marks.values())[0]
            student_Mark_subject.marks = sum(marks)

            print(student_Mark_subject.total_marks, '================total marks=============', sum(marks))

            student_grade = (student_Mark_subject.total_marks / student_Mark_subject.marks) * 100
            print("percentage=======4======", student_grade)
            if student_grade >= 100:
                student_Mark_subject.grade = "A"
            elif student_grade >= 80:
                student_Mark_subject.grade = "B"
            elif student_grade >= 60:
                student_Mark_subject.grade = "C"
            elif student_grade >= 40:
                student_Mark_subject.grade = "D"
            elif student_grade >= 35:
                student_Mark_subject.grade = "F"
            else:
                student_Mark_subject.grade = ''
            student_Mark_subject.save()

            student_Mark_subject.subjects.add(instance.id)


# </editor-fold>


# <editor-fold desc="WHEN USER IS CREATED THEN STUDENT AND SUBJECT AND MARKS IN USER INSTANCE IS CREATED">
def marks_post_save_receiver(sender, created, instance, *args, **kwargs):
    if created:
        try:
            student = studentStudentModel.objects.get(student=instance)
        except:
            student = studentStudentModel.objects.create(student=instance)

        if student:
            try:
                subject = studentSubjectsModel.objects.get(student=instance)
            except:
                subject = studentSubjectsModel.objects.create(student=instance)
            print(subject, '====================')

        if subject:
            try:
                marks = studentMarksModel.objects.get(student=student)
            except:
                marks = studentMarksModel.objects.create(student=student)

            marks.subjects.add(subject)
        # else:
        #     student.delete()


# </editor-fold>


# <editor-fold desc="WHEN STUDENT SUBJECT IS DELETED THEN STUDENT MARKS ALSO UPDATED">
def subject_post_delete_receiver(sender, instance, *args, **kwargs):
    # write your login when user profile is deleted.
    print("student subject Deleted")
    if instance:
        totalmarks = studentSubjectsModel.objects.all().filter(student=instance.student).values_list('score_marks',
                                                                                                     flat=True)
        marks = studentSubjectsModel.objects.all().filter(student=instance.student).values_list('marks', flat=True)
        print(sum(totalmarks))
        print(sum(marks))
    try:
        student = studentStudentModel.objects.get(student=instance.student)
        print(student, '================================================')
    except:
        pass

    try:
        if student is not None:
            studentMarksModel.objects.filter(student=student).update(total_marks=sum(totalmarks), marks=sum(marks))
        else:
            studentMarksModel.objects.filter(student=student).update(total_marks=sum(totalmarks), marks=sum(marks),
                                                                     grade='')
    except:
        pass


# </editor-fold>

# <editor-fold desc="WHEN USER IS CREATED THEN STUDENT SUBJECT CREATED ">
def student_subject_post_save_receiver(sender, created, instance, *args, **kwargs):
    if created:
        studentSubjectsModel.objects.create(student=instance)


# </editor-fold>


# Create your models here.
# <editor-fold desc="STUDENT">
class studentStudentModel(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, related_name="studentStudentModel_student")
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.student)


pre_save.connect(slug_pre_save_receiver, sender=studentStudentModel)
post_save.connect(student_post_save_receiver, sender=User)


# </editor-fold>


# <editor-fold desc="SUBJECTS">
class studentSubjectsModel(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="studentSubjectsModel_student")
    subject = models.CharField(max_length=200)
    marks = models.PositiveSmallIntegerField(default=100)
    score_marks = models.PositiveSmallIntegerField(default=0)
    subject_code = models.CharField(_('subject ID'), max_length=13, unique=True, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.student) + str(self.subject)


pre_save.connect(slug_pre_save_receiver, sender=studentSubjectsModel)
pre_save.connect(subject_code_unique_code_generator, sender=studentSubjectsModel)

post_save.connect(subject_post_save_receiver, sender=studentSubjectsModel)
post_delete.connect(subject_post_delete_receiver, sender=studentSubjectsModel)
post_save.connect(student_subject_post_save_receiver, sender=User)


# </editor-fold>


# <editor-fold desc="MARKS">
class studentMarksModel(models.Model):
    student = models.OneToOneField(studentStudentModel, on_delete=models.CASCADE,
                                   related_name="studentMarksModel_student", unique=True)
    subjects = models.ManyToManyField(studentSubjectsModel,
                                      related_name="studentMarksModel_subjects")
    marks = models.PositiveSmallIntegerField(default=0)
    total_marks = models.PositiveSmallIntegerField(default=0)
    grade = models.CharField(max_length=20, choices=studentGradeEnumTypes.choices(), null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, null=True, unique=True, blank=True)

    def __str__(self):
        return str(self.student)

    # def get_subjects(self,obj):
    #     subjects=self.subjects.subject
    #     print("subjects",subjects)
    #     return subjects


pre_save.connect(slug_pre_save_receiver, sender=studentMarksModel)
post_save.connect(marks_post_save_receiver, sender=User)

# </editor-fold>
