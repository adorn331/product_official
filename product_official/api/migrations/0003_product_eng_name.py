# Generated by Django 2.0.4 on 2018-08-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180617_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='eng_name',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]