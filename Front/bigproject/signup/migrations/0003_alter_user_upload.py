# Generated by Django 4.1.3 on 2022-12-12 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_user_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]