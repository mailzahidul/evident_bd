# Generated by Django 4.1.4 on 2023-07-24 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0008_remove_userprofile_common_ptr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
    ]
