# Generated by Django 3.2.7 on 2022-07-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='flagged',
            field=models.BooleanField(default=False),
        ),
    ]