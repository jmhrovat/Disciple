# Generated by Django 3.1.5 on 2021-04-29 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='profiles',
            field=models.ManyToManyField(through='tasks.TaskStatus', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='taskstatus',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]