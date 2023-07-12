# Generated by Django 4.2.2 on 2023-06-27 06:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='freatured_image',
            new_name='big_img',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='discription',
            new_name='discription_first',
        ),
        migrations.RemoveField(
            model_name='add_info',
            name='info',
        ),
        migrations.AddField(
            model_name='add_info',
            name='brand',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='add_info',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='add_info',
            name='dimensions',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='add_info',
            name='size',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='add_info',
            name='weight',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Product_quality',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='discription_second',
            field=ckeditor.fields.RichTextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='discription_third',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='small_img_first',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='small_img_second',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=500, null=True, unique=True),
        ),
    ]