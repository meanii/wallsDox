# Generated by Django 3.2.5 on 2021-08-11 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UsersAccount',
        ),
    ]