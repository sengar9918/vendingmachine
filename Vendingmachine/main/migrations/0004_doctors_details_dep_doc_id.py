# Generated by Django 4.1.5 on 2023-01-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors_details',
            name='dep_doc_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
