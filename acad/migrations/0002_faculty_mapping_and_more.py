# Generated by Django 4.2.8 on 2024-01-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("acad", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Faculty_Mapping",
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
                ("faculty_id", models.CharField(max_length=10)),
                ("branch", models.CharField(max_length=60)),
                ("semester", models.IntegerField()),
                ("section", models.CharField(max_length=1)),
                ("course_code", models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name="marks", old_name="external_marks", new_name="cia_marks",
        ),
        migrations.RenameField(
            model_name="marks", old_name="internal_marks", new_name="end_exam_marks",
        ),
    ]
