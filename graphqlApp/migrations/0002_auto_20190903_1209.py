# Generated by Django 2.2.5 on 2019-09-03 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphqlApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='change_type',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='newvalue',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='oldvalue',
        ),
    ]