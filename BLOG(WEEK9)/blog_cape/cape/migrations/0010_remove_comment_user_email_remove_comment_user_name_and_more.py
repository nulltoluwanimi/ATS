# Generated by Django 4.0.6 on 2022-08-05 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cape', '0009_rename_is_archieved_post_is_archived'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
