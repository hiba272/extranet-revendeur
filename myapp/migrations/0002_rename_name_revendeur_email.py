# Generated by Django 5.0.7 on 2024-07-28 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revendeur',
            old_name='name',
            new_name='email',
        ),
    ]
