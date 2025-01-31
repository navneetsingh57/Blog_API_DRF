# Generated by Django 5.1.4 on 2024-12-22 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=200)),
                ('report', models.PositiveSmallIntegerField(choices=[(1, 'Bulying or unwanted content'), (2, 'Suicide, self-injury'), (3, 'Nudity or sexual activity'), (4, 'Scam, fraud, false information')], default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('excerpt', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='posts')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('reported', models.BooleanField(default=False)),
            ],
        ),
    ]
