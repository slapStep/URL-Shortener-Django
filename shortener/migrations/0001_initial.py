# Generated by Django 4.0.1 on 2022-01-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('times_followed', models.PositiveIntegerField(default=0)),
                ('long_url', models.URLField()),
                ('short_url', models.CharField(blank=True, max_length=15, unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
