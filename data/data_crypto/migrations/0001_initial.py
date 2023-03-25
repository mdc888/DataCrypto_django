# Generated by Django 4.1.5 on 2023-03-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_crypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
    ]
