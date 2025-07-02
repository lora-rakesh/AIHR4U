from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company
from .serializers import CompanyVerifySerializer

from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator


@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"message": "✅ CSRF cookie set"})


@method_decorator(ensure_csrf_cookie, name='dispatch')
class CompanyVerifyAPIView(GenericAPIView):
    serializer_class = CompanyVerifySerializer

    def get(self, request):
        return Response({
            "message": "Send a POST request with {'name': 'Your Company Name'} to verify."
        })

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            company_name = serializer.validated_data['company_name']
            exists = Company.objects.filter(name__iexact=company_name).exists()
            if exists:
                return Response(
                    {"message": "✅ Company Verified"},
                    status=status.HTTP_200_OK
                )
            return Response(
                {"message": "❌ Company Not Found"},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

