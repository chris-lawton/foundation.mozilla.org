# Generated by Django 2.2.5 on 2019-10-16 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0030_product_parental_controls_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprivacypolicylink',
            name='url',
            field=models.URLField(blank=True, help_text='Privacy policy URL', max_length=2048),
        ),
    ]
