# Generated by Django 4.2 on 2024-11-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_mynotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('msg', models.TextField()),
            ],
        ),
    ]
