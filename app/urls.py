from django.urls import path
from .views import CompanyVerifyAPIView, get_csrf_token, EmployeeLoginAPIView

urlpatterns = [
    path('verify-company/', CompanyVerifyAPIView.as_view(), name='verify-company'),
    path('login/', EmployeeLoginAPIView.as_view(), name='employee-login'),
    path('get-csrf/', get_csrf_token, name='get-csrf-token'),
]
