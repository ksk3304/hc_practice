# Generated by Django 4.2.17 on 2025-01-08 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='contents',
            field=models.TextField(blank=True, null=True),
        ),
    ]