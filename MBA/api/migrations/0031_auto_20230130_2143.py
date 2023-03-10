# Generated by Django 3.2.7 on 2023-01-30 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0030_alter_img_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pp',
            field=models.ImageField(null=True, upload_to='static/profilepictures'),
        ),
        migrations.AlterField(
            model_name='img',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
