# Generated by Django 2.0.2 on 2018-03-19 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180319_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_dated',
            new_name='created_date',
        ),
    ]
