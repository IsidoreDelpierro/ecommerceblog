# Generated by Django 4.0.6 on 2022-09-15 10:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_product_rating_manual_review'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0022_alter_profile_bio'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Profiler',
        ),
    ]
