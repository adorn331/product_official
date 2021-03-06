# Generated by Django 2.0.4 on 2018-06-06 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('version', models.CharField(max_length=64)),
                ('profile', models.TextField(blank=True)),
                ('home_picture', models.FileField(upload_to='images/home_picture/%Y/%m/%d')),
                ('QRcode', models.FileField(upload_to='images/QRcode/%Y/%m/%d')),
                ('icon', models.FileField(upload_to='images/icon/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='APP',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Product')),
                ('apk_file', models.FileField(upload_to='files/app/apk_file/%Y/%m/%d')),
                ('apple_store_url', models.URLField(max_length=2000)),
                ('android_store_url', models.URLField(max_length=2000)),
            ],
            bases=('api.product',),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Product')),
                ('android_file', models.FileField(blank=True, upload_to='', verbose_name='files/game/android_file/%Y/%m/%d')),
                ('windows_file', models.FileField(blank=True, upload_to='', verbose_name='files/game/windows_file/%Y/%m/%d')),
                ('macOS_file', models.FileField(blank=True, upload_to='', verbose_name='files/game/macOS_file/%Y/%m/%d')),
            ],
            bases=('api.product',),
        ),
        migrations.CreateModel(
            name='H5',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Product')),
            ],
            bases=('api.product',),
        ),
        migrations.CreateModel(
            name='LittleProgram',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Product')),
            ],
            bases=('api.product',),
        ),
    ]
