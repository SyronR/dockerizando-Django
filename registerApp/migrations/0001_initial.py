# Generated by Django 4.1.13 on 2023-12-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('username', models.TextField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('password', models.TextField(max_length=50)),
            ],
        ),
    ]
