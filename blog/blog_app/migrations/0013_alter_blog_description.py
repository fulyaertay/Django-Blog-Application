# Generated by Django 3.2.9 on 2021-12-16 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0012_auto_20211216_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Blog İçeriği:'),
        ),
    ]
