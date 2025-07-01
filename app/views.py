from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company
from .serializers import CompanyVerifySerializer

class CompanyVerifyAPIView(GenericAPIView):
    serializer_class = CompanyVerifySerializer

    def get(self, request):
        return Response({
            "message": "Submit POST request with 'company_name' to verify."
        })

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "✅ Company Verified"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
