# Generated by Django 5.1.3 on 2024-11-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_rename_taks_id_todomodel_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='completed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]