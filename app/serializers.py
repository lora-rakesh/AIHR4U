from rest_framework import serializers
from .models import Company, Employee

# Company Verification Serializer
class CompanyVerifySerializer(serializers.Serializer):
    company_name = serializers.CharField()

    def validate_company_name(self, value):
        if not Company.objects.filter(name__iexact=value.strip()).exists():
            raise serializers.ValidationError("❌ Company not found")
        return value

# Login Serializer
class LoginSerializer(serializers.Serializer):
    employee_id = serializers.CharField()
    password = serializers.CharField(write_only=True)

# Profile Picture Serializer
class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['profile_picture']
    