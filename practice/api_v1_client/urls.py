from django.urls import path, include

from .views import accountsClientUserCreateGenericsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # <editor-fold desc="USER REGISTER">
    path('user-create/', accountsClientUserCreateGenericsView.as_view(), name='accountsClientUserCreateGenericsViewURL'),
    # </editor-fold>

    # <editor-fold desc="USER LOGIN WITH ACCESS TOKEN">
    path('user-login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # </editor-fold>

    # <editor-fold desc="USER LOGIN WITH REFRESH TOKEN ,WHEN ACCESS TOKEN IS EXPIRED ">
    path('user-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # </editor-fold>



]
