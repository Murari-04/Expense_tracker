# Generated by Django 5.2.4 on 2025-07-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_trackinghistory_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackinghistory',
            name='amount',
            field=models.FloatField(),
        ),
    ]
