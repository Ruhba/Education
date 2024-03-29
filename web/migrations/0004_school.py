# Generated by Django 4.2.4 on 2024-01-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_facilities_colour'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/school')),
                ('name', models.CharField(max_length=100)),
                ('Timage', models.ImageField(upload_to='media/Teachers')),
                ('Tname', models.CharField(max_length=150)),
                ('Coursefee', models.IntegerField()),
                ('age', models.IntegerField()),
                ('Time', models.IntegerField()),
                ('Capacity', models.IntegerField()),
            ],
        ),
    ]
