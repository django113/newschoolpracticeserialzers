from django.urls import path

from student.api_v1_admin.views import studentAdminMarksCreateGenericsView, studentAdminMarksDetailsAPIView, \
    studentAdminSubjectCreateGenericsView

urlpatterns = [

    # <editor-fold desc="MARKS GET AND CREATE BY USING STUDENT SLUG">
    path('marks-create/', studentAdminMarksCreateGenericsView.as_view(),
         name="studentAdminMarksCreateGenericsViewURL"),
    # </editor-fold>


    # <editor-fold desc="MARKS GET DETAILS BY USING MARKS SLUG">
    path('marks-details/<slug>/', studentAdminMarksDetailsAPIView.as_view(),
         name="studentAdminMarksDetailsAPIViewURL"),
    # </editor-fold>

    # <editor-fold desc="SUBJECT CREATE BY ADMIN">
    path('subject-create/',studentAdminSubjectCreateGenericsView.as_view(),
         name="studentAdminSubjectCreateGenericsViewURL")
    # </editor-fold>

]
