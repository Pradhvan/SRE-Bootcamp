from rest_framework import serializers
from ..models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        read_only_fields = ("id", "created_date", "updated_date", "enrollment_date",)
        exclude = ("id", "is_active",)