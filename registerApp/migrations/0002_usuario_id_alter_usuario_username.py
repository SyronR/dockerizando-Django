# Generated by Django 4.1.13 on 2023-12-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.TextField(max_length=50, unique=True),
        ),
    ]