# Generated by Django 2.0.4 on 2018-04-27 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
