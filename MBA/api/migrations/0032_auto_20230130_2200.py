# Generated by Django 3.2.7 on 2023-01-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20230130_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recharge',
            old_name='user',
            new_name='host',
        ),
        migrations.AlterField(
            model_name='img',
            name='user',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
