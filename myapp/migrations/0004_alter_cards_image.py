# Generated by Django 4.2 on 2023-04-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_cards_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
