# Generated by Django 4.0.6 on 2022-09-15 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_remove_profiler_user'),
        ('store', '0012_alter_order_customer_alter_review_customer_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profiler',
        ),
    ]
