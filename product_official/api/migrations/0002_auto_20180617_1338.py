# Generated by Django 2.0.4 on 2018-06-17 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='android_file',
            field=models.FileField(blank=True, upload_to='files/game/android_file/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='game',
            name='macOS_file',
            field=models.FileField(blank=True, upload_to='files/game/macOS_file/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='game',
            name='windows_file',
            field=models.FileField(blank=True, upload_to='files/game/windows_file/%Y/%m/%d'),
        ),
    ]
