# Generated by Django 4.0.5 on 2022-07-05 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_agent_rename_price_exception_listing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
