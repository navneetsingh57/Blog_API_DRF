# Generated by Django 5.1.4 on 2024-12-25 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_date_joined_user_modified_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]
