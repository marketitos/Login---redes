# Generated by Django 4.2 on 2023-04-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_cards_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='image',
            field=models.FileField(blank=True, upload_to='images'),
        ),
    ]
