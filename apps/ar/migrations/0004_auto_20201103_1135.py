# Generated by Django 3.1.2 on 2020-11-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ar', '0003_auto_20201103_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ar',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='ar',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
