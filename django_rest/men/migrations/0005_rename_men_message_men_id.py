# Generated by Django 4.2.4 on 2023-08-14 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0004_rename_category_men_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='men',
            new_name='men_id',
        ),
    ]
