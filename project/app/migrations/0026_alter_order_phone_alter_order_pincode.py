# Generated by Django 4.2.2 on 2023-07-06 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_order_paid_order_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]