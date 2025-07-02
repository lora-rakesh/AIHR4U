from django.urls import path
from .views import CompanyVerifyAPIView, get_csrf_token

urlpatterns = [
    path('verify-company/', CompanyVerifyAPIView.as_view(), name='verify-company'),
    path('get-csrf/', get_csrf_token, name='get-csrf-token'),
]
