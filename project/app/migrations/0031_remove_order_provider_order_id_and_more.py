# Generated by Django 4.2.2 on 2023-07-07 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_order_provider_order_id_order_signature_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='provider_order_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='signature_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='razor_pay_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='razor_pay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='razor_pay_payment_signature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]