# Generated by Django 3.0.1 on 2020-01-31 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examcard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=190)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examcard.StudentProfile')),
            ],
            options={
                'verbose_name': 'StudentUnit',
                'verbose_name_plural': 'StudentUnits',
            },
        ),
    ]
