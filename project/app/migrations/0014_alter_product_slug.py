# Generated by Django 4.2.2 on 2023-06-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', max_length=500, null=True, unique=True),
        ),
    ]