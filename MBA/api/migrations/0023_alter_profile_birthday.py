# Generated by Django 3.2.7 on 2023-01-30 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20230130_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.CharField(max_length=20, null=True),
        ),
    ]