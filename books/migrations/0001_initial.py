# Generated by Django 4.1.3 on 2022-12-05 02:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=100)),
                ("summary", models.TextField(blank=True, null=True)),
                ("isbn", models.CharField(max_length=50)),
                ("genre", models.TextField(blank=True, null=True)),
            ],
        ),
    ]