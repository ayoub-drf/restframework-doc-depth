# Generated by Django 5.1.2 on 2024-11-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_author_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
