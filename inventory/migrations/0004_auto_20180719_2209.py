# Generated by Django 2.0.7 on 2018-07-19 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20180626_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entity',
            old_name='ids',
            new_name='canonical_facts',
        ),
    ]