# Generated by Django 3.2 on 2023-08-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_auto_20230811_1449"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="email"),
        ),
    ]
