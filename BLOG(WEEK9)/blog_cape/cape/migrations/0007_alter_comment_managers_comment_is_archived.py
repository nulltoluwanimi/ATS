# Generated by Django 4.0.6 on 2022-08-04 13:09

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('cape', '0006_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('archived_comments', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
