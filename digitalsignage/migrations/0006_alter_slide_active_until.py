# Generated by Django 4.1.7 on 2023-03-19 01:07

import digitalsignage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalsignage', '0005_slide_active_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='active_until',
            field=models.DateTimeField(blank=True, default=digitalsignage.models.one_month_from_today, null=True),
        ),
    ]
