# Generated by Django 4.1.3 on 2022-12-07 15:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_bookitem"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BookItem",
        ),
    ]
