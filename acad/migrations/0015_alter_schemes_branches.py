# Generated by Django 4.2.5 on 2024-01-25 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0014_alter_subjects_scheme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemes',
            name='branches',
            field=models.TextField(help_text='Enter branches seperated by space..'),
        ),
    ]
