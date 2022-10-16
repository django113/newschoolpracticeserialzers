from django.urls import path

from student.api_v1_client.views import studentClientStudentCreateGenericsView, studentClientSubjectCreateGenericsView, \
    studentClientStudentDetailsAPIView, studentClientMarksDetailsAPIView

urlpatterns = [

    # <editor-fold desc="STUDENT CREATE AND GET THE LIST">
    path('student-create/', studentClientStudentCreateGenericsView.as_view(),
         name="studentClientStudentCreateGenericsViewURL"),
    # </editor-fold>
    # <editor-fold desc="STUDENT DETAILS BY USING STUDENT SLUG">
    path('student-details/<slug>/', studentClientStudentDetailsAPIView.as_view(),
         name="studentClientStudentDetailsAPIViewURL"),
    # </editor-fold>

    # <editor-fold desc="SUBJECT CREATE AND GET ALL SUBJECTS">
    path('subject-create/', studentClientSubjectCreateGenericsView.as_view(),
         name="studentClientSubjectCreateGenericsViewURL"),
    # </editor-fold>

    # <editor-fold desc="GET MARKS DETAILS BY USING MARKS SLUG">
    path('marks-details/<slug>/', studentClientMarksDetailsAPIView.as_view(),
         name="studentClientMarksDetailsAPIViewURL"),
    # </editor-fold>

]
