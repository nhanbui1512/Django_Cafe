# Generated by Django 4.1.7 on 2023-03-28 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_category_product_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Url_Image',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]