# Generated by Django 4.2.4 on 2023-08-14 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0005_rename_men_message_men_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='men',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='men_id',
            new_name='men',
        ),
    ]
