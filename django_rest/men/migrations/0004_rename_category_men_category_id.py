# Generated by Django 4.2.4 on 2023-08-14 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0003_remove_men_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='men',
            old_name='category',
            new_name='category_id',
        ),
    ]
