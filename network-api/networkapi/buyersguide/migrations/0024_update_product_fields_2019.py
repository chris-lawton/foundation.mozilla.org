# Generated by Django 2.2.5 on 2019-10-09 00:10

from django.db import migrations, models
import networkapi.buyersguide.models


class Migration(migrations.Migration):

    dependencies = [
        ('buyersguide', '0023_auto_20190917_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='collects_biometrics',
            field=networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does this product collect biometric data?'),
        ),
        migrations.AddField(
            model_name='product',
            name='collects_biometrics_helptext',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='product',
            name='how_does_it_share',
            field=models.CharField(blank=True, help_text='How does this product handle data?', max_length=5000),
        ),
        migrations.AddField(
            model_name='product',
            name='privacy_policy',
            field=networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does this product have a privacy policy?'),
        ),
        migrations.AddField(
            model_name='product',
            name='user_friendly_privacy_policy',
            field=networkapi.buyersguide.fields.ExtendedYesNoField(help_text='Does this product have a user-friendly privacy policy?'),
        ),

        # A boatload of fields were using blank="True" rather than blank=True

        migrations.AlterField(
            model_name='product',
            name='blurb',
            field=models.TextField(blank=True, help_text='Description of the product', max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='child_rules_helptext',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.CharField(blank=True, help_text='Name of Company', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='delete_data_helptext',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='email',
            field=models.CharField(blank=True, help_text='Email', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='live_chat',
            field=models.CharField(blank=True, help_text='Live Chat', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='manage_security_helptext',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='must_change_default_password_helptext',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, help_text='Name of Product', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Phone Number', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, help_text='Price', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='privacy_policy_helptext',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='privacy_policy_reading_level_url',
            field=models.URLField(blank=True, help_text='Link to privacy policy reading level', max_length=2048),
        ),
        migrations.AlterField(
            model_name='product',
            name='privacy_policy_url',
            field=models.URLField(blank=True, help_text='Link to privacy policy', max_length=2048),
        ),
        migrations.AlterField(
            model_name='product',
            name='security_updates_helptext',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='share_data_helptext',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='twitter',
            field=models.CharField(blank=True, help_text='Twitter username', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(blank=True, help_text='Link to this product page', max_length=2048),
        ),
        migrations.AlterField(
            model_name='product',
            name='uses_encryption_helptext',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='worst_case',
            field=models.CharField(blank=True, help_text="What's the worst thing that could happen by using this product?", max_length=5000),
        ),
        migrations.AlterField(
            model_name='update',
            name='author',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='update',
            name='snippet',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='update',
            name='source',
            field=models.URLField(blank=True, help_text='Link to source', max_length=2048),
        ),
        migrations.AlterField(
            model_name='update',
            name='title',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]