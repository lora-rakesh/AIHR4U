from rest_framework import serializers
from .models import Company

class CompanyVerifySerializer(serializers.Serializer):
    company_name = serializers.CharField()

    def validate_company_name(self, value):
        if not Company.objects.filter(name__iexact=value.strip()).exists():
            raise serializers.ValidationError("❌ Company not found")
        return value
# serializers.py
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    employee_id = serializers.CharField()
    password = serializers.CharField(write_only=True)
