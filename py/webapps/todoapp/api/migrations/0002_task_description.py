# Generated by Django 3.1.4 on 2021-01-03 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]