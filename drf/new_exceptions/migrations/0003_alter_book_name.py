# Generated by Django 5.1.2 on 2024-11-28 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_exceptions', '0002_alter_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
