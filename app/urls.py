from django.urls import path
from .views import CompanyVerifyAPIView

urlpatterns = [
    path('verify-company/', CompanyVerifyAPIView.as_view(), name='verify-company'),
]
