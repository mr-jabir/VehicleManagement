# Generated by Django 3.2.10 on 2023-05-18 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0002_userdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdb',
            name='confirmpassword',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
