# Generated by Django 3.0.1 on 2020-01-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examcard', '0003_auto_20200131_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='unit_code',
            field=models.CharField(default=12, max_length=191),
            preserve_default=False,
        ),
    ]