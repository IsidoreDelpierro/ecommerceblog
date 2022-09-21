# Generated by Django 4.0.6 on 2022-09-15 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name of Business', max_length=200)),
                ('subname', models.CharField(default='Your Slogan', max_length=200)),
                ('about', models.CharField(default='About the Business', max_length=500)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('slogan', models.CharField(default='Slogan', max_length=200)),
                ('logo', models.ImageField(upload_to='images/logo/')),
                ('website_url', models.CharField(default='#', max_length=255)),
                ('facebook_url', models.CharField(default='https://www.facebook.com/', max_length=255)),
                ('twitter_url', models.CharField(default='https://www.twitter.com/', max_length=255)),
                ('instagram_url', models.CharField(default='https://www.instagram.com/', max_length=255)),
                ('pinterest_url', models.CharField(default='https://www.pinterest.com/', max_length=255)),
                ('tiktok_url', models.CharField(default='https://www.tiktok.com/', max_length=255)),
                ('youtube_url', models.CharField(default='https://www.youtube.com/', max_length=255)),
                ('blogger_url', models.CharField(default='https://www.blogger.com/', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Business',
            },
        ),
    ]
