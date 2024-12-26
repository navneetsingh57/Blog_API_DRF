# Generated by Django 5.1.4 on 2024-12-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
