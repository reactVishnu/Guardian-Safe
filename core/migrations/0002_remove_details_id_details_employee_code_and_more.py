# Generated by Django 4.2.7 on 2023-12-02 19:33

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='id',
        ),
        migrations.AddField(
            model_name='details',
            name='employee_code',
            field=models.CharField(default='emp0000', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='aadhar_file',
            field=models.FileField(blank=True, null=True, storage=core.models.OverwriteStorage, upload_to=core.models.user_aadhar_upload_path),
        ),
        migrations.AlterField(
            model_name='details',
            name='pan_file',
            field=models.FileField(blank=True, null=True, storage=core.models.OverwriteStorage, upload_to=core.models.user_pan_upload_path),
        ),
    ]
