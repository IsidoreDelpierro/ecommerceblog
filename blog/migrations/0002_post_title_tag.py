# Generated by Django 4.0.6 on 2022-08-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='eCommerce Blog', max_length=255),
        ),
    ]
