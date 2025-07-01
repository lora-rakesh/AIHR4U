from rest_framework import serializers
from .models import Company

class CompanyVerifySerializer(serializers.Serializer):
    company_name = serializers.CharField()

    def validate_company_name(self, value):
        if not Company.objects.filter(name__iexact=value.strip()).exists():
            raise serializers.ValidationError("❌ Company not found")
        return value
