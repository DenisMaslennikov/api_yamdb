# Generated by Django 3.2 on 2023-08-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.SlugField(
                choices=[
                    ("user", "user"),
                    ("admin", "admin"),
                    ("moderator", "moderator"),
                ],
                default="user",
            ),
        ),
    ]
