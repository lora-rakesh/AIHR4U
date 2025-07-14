from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Company, Employee
from .serializers import (
    CompanyVerifySerializer,
    LoginSerializer,
    ProfilePhotoSerializer
)

# CSRF Token Setup
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"message": "✅ CSRF cookie set"})

# Company Verification View
@method_decorator(ensure_csrf_cookie, name='dispatch')
class CompanyVerifyAPIView(GenericAPIView):
    serializer_class = CompanyVerifySerializer

    def get(self, request):
        return Response({
            "message": "Send a POST request with {'company_name': 'Your Company Name'} to verify."
        })

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            company_name = serializer.validated_data['company_name']
            exists = Company.objects.filter(name__iexact=company_name).exists()
            if exists:
                return Response({"message": "✅ Company Verified"}, status=status.HTTP_200_OK)
            return Response({"message": "❌ Company Not Found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Employee Login View
class EmployeeLoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            employee_id = serializer.validated_data['employee_id']
            password = serializer.validated_data['password']
            user = authenticate(request, username=employee_id, password=password)
            if user and isinstance(user, Employee):
                login(request, user)  # Session login
                return Response({
                    'message': '✅ Login successful',
                    'employee_id': user.employee_id,
                    'name': user.name,
                }, status=status.HTTP_200_OK)
            return Response({'error': '❌ Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Profile Photo Create View
class CreateProfilePhotoAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfilePhotoSerializer

    def post(self, request):
        employee = get_object_or_404(Employee, employee_id=request.user.employee_id)
        serializer = self.get_serializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '✅ Profile photo uploaded successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Profile Photo Update View
class UpdateProfilePhotoAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfilePhotoSerializer

    def put(self, request):
        employee = get_object_or_404(Employee, employee_id=request.user.employee_id)
        serializer = self.get_serializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '✅ Profile photo updated successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Profile Photo Delete View
class DeleteProfilePhotoAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfilePhotoSerializer

    def delete(self, request):
        employee = get_object_or_404(Employee, employee_id=request.user.employee_id)
        if employee.profile_picture:
            employee.profile_picture.delete(save=True)
            return Response({'message': '🗑️ Profile photo deleted successfully.'}, status=status.HTTP_200_OK)
        return Response({'error': '⚠️ No profile photo to delete.'}, status=status.HTTP_400_BAD_REQUEST)
