# Generated by Django 4.2.1 on 2023-06-01 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_user_alter_cards_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
