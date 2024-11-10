# Generated by Django 5.1.2 on 2024-11-09 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_child_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('file', models.FileField(upload_to='media/files')),
            ],
        ),
    ]
