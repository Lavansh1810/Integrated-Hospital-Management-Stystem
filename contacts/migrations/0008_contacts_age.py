# Generated by Django 4.1.1 on 2022-11-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_contacts_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
