# Generated by Django 3.2.2 on 2021-07-07 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_catogary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catogary',
            new_name='category',
        ),
    ]
