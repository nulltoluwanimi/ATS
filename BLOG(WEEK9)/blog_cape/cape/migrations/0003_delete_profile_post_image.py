# Generated by Django 4.0.6 on 2022-08-02 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cape', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]