# Generated by Django 4.2.5 on 2023-09-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Food",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=500)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="uploads/"),
                ),
                ("calories", models.IntegerField(default=0)),
                ("carbohydrates", models.IntegerField(default=0)),
                ("proteins", models.IntegerField(default=0)),
                ("fats", models.IntegerField(default=0)),
            ],
        ),
    ]