# Generated by Django 4.2.2 on 2023-06-26 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_a_i_add_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]