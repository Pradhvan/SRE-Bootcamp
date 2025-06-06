# Generated by Django 5.1.6 on 2025-03-05 11:05

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "student_id",
                    models.CharField(
                        max_length=20,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Student ID must be 2 letters followed by 10 digits",
                                regex="^[A-Z]{2}\\d{10}$",
                            )
                        ],
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        unique=True,
                        validators=[django.core.validators.EmailValidator()],
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        help_text="Indian phone number with +91 prefix (10 digits starting with 6-9)",
                        max_length=15,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Enter a valid Indian phone number",
                                regex="^\\+91\\s?[6-9]\\d{9}$",
                            )
                        ],
                    ),
                ),
                ("date_of_birth", models.DateField()),
                (
                    "biological_sex",
                    models.CharField(
                        choices=[
                            ("MALE", "male"),
                            ("FEMALE", "female"),
                            ("OTHER", "other"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "grade_level",
                    models.IntegerField(help_text="Current grade level of the student"),
                ),
                (
                    "enrollment_date",
                    models.DateField(default=django.utils.timezone.now),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Students",
                "indexes": [
                    models.Index(
                        fields=["student_id"], name="student_stu_student_bb3d1e_idx"
                    )
                ],
            },
        ),
    ]
