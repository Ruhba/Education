# Generated by Django 4.2.4 on 2024-01-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_teachers_alter_school_time_alter_school_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='insta',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
