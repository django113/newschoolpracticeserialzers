from django.urls import path, include

# THIS IS NOT INCLUDED


urlpatterns = [

    # <editor-fold desc="user register">
    path('api/client/v1/', include('practice.api_v1_client.urls')),
    # </editor-fold>




]
