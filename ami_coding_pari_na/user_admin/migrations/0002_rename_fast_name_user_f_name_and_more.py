# Generated by Django 4.0.5 on 2022-06-26 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fast_name',
            new_name='f_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='l_name',
        ),
    ]
