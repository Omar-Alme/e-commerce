# Generated by Django 4.2.7 on 2024-02-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_options_option_category'),
        ('orders', '0003_remove_orderitem_colour_remove_orderitem_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product_options',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='options',
            field=models.ManyToManyField(blank=True, to='product.product_options'),
        ),
    ]
