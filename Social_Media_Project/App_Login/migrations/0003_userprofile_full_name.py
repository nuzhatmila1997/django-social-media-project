# Generated by Django 3.0.8 on 2020-07-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0002_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
