from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    CompanyVerifyAPIView,
    get_csrf_token,
    EmployeeLoginAPIView,
    CreateProfilePhotoAPIView,
    UpdateProfilePhotoAPIView,
    DeleteProfilePhotoAPIView,
)

urlpatterns = [
    path('verify-company/', CompanyVerifyAPIView.as_view(), name='verify-company'),
    path('login/', EmployeeLoginAPIView.as_view(), name='employee-login'),
    path('get-csrf/', get_csrf_token, name='get-csrf-token'),

    # Profile Photo APIs
    path('profile-photo/create/', CreateProfilePhotoAPIView.as_view(), name='create-profile-photo'),
    path('profile-photo/update/', UpdateProfilePhotoAPIView.as_view(), name='update-profile-photo'),
    path('profile-photo/delete/', DeleteProfilePhotoAPIView.as_view(), name='delete-profile-photo'),


     # JWT Token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
