# Generated by Django 5.1.4 on 2025-01-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='daha_öge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('güncelemeler', models.CharField(max_length=100)),
                ('yenilik', models.TextField(default='Çok yakında...')),
            ],
        ),
    ]
