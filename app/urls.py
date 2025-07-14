from django.urls import path
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

    # Profile photo APIs
    path('profile-photo/create/', CreateProfilePhotoAPIView.as_view(), name='create-profile-photo'),
    path('profile-photo/update/', UpdateProfilePhotoAPIView.as_view(), name='update-profile-photo'),
    path('profile-photo/delete/', DeleteProfilePhotoAPIView.as_view(), name='delete-profile-photo'),
]
