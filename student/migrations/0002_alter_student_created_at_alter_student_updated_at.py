# Generated by Django 5.1.6 on 2025-03-05 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="updated_at",
            field=models.DateField(auto_now=True),
        ),
    ]
