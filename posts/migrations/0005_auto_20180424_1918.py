# Generated by Django 2.0.4 on 2018-04-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180424_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, default='download.jpg', upload_to=''),
        ),
    ]
