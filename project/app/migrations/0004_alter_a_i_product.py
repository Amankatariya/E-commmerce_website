# Generated by Django 4.2.2 on 2023-06-26 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_product_product_information_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a_i',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
    ]