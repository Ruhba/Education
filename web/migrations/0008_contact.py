# Generated by Django 4.2.4 on 2024-01-27 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_clients_remove_teachers_insta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guardian_name', models.CharField(max_length=100)),
                ('guardian_email', models.CharField(max_length=100)),
                ('child_name', models.CharField(max_length=100)),
                ('child_age', models.IntegerField()),
                ('message', models.CharField(max_length=300)),
            ],
        ),
    ]