# Generated by Django 3.2.9 on 2021-11-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover_photo',
            field=models.FileField(upload_to='images/'),
        ),
    ]
