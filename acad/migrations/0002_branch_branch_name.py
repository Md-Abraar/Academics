# Generated by Django 4.2.8 on 2024-01-29 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("acad", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="branch",
            name="branch_name",
            field=models.CharField(
                default="Computer Science and Engineering", max_length=60
            ),
            preserve_default=False,
        ),
    ]