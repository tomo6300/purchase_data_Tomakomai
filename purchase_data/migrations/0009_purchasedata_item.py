# Generated by Django 3.2 on 2022-12-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_data', '0008_auto_20221210_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedata',
            name='item',
            field=models.ManyToManyField(blank=True, related_name='purchase_data', to='purchase_data.Item', verbose_name='購入商品'),
        ),
    ]
