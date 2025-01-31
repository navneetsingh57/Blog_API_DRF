# Generated by Django 5.1.4 on 2024-12-24 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('blog', '0006_alter_comment_comment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.CharField(blank=True, default=None, max_length=200),
            preserve_default=False,
        ),
    ]
