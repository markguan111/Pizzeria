# Generated by Django 3.0.5 on 2021-12-12 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0006_auto_20211212_0127'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewComment',
            new_name='Comment',
        ),
    ]
