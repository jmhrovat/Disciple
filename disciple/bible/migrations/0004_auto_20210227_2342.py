# Generated by Django 3.1.5 on 2021-02-27 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0003_kjv_verse_verse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kjv_verse',
            name='verse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kjv_verse', to='bible.verse'),
        ),
    ]
