# Generated by Django 4.1.3 on 2022-11-22 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LocalServicesBoard', '0004_rename_text_review_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='classified',
            name='phone',
            field=models.CharField(default='', max_length=30),
        ),
    ]
