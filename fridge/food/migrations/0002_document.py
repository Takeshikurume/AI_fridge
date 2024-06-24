# Generated by Django 4.1 on 2024-06-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Document",
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
                ("description", models.CharField(blank=True, max_length=255)),
                ("photo", models.ImageField(default="defo", upload_to="documents/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "output",
                    models.ImageField(default="output/output.jpg", upload_to=""),
                ),
            ],
        ),
    ]
