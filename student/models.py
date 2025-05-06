from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, EmailValidator


class BiologicalSexChoices(models.TextChoices):
    MALE = "MALE", "male"
    FEMALE = "FEMALE", "female"
    OTHER = "OTHER", "other"


class Student(models.Model):
    name = models.CharField(max_length=50)
    student_id = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[A-Z]{2}\d{10}$",
                message="Student ID must be 2 letters followed by 10 digits",
            )
        ],
    )
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^\+91\s?[6-9]\d{9}$",
                message="Enter a valid Indian phone number",
            )
        ],
        help_text="Indian phone number with +91 prefix (10 digits starting with 6-9)",
    )
    date_of_birth = models.DateField()
    biological_sex = models.CharField(
        max_length=20, choices=BiologicalSexChoices.choices
    )
    grade_level = models.IntegerField(help_text="Current grade level of the student")
    enrollment_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.student_id} ({self.name})"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        indexes = [
            models.Index(fields=["student_id"]),
        ]
