from django.urls import path, include

urlpatterns = [

    # <editor-fold desc="STUDENT">
    path('api/client/v1/', include('student.api_v1_client.urls')),
    # </editor-fold>

    # <editor-fold desc="STUDENT">
    path('api/admin/v1/', include('student.api_v1_admin.urls')),
    # </editor-fold>

]