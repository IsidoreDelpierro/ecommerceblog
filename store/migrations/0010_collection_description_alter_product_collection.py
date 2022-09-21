# Generated by Django 4.0.6 on 2022-09-08 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.CharField(blank=True, default='Describe this collection', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.collection'),
        ),
    ]
