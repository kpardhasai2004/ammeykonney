# Generated by Django 4.2 on 2023-04-18 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
