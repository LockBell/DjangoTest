# Generated by Django 4.1.1 on 2022-09-22 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.CharField(max_length=256, unique=True)),
                ('password', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
