# Generated by Django 5.1.2 on 2024-11-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='father',
            name='name',
        ),
        migrations.AddField(
            model_name='father',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
