# Generated by Django 3.1.5 on 2021-09-25 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20210924_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Male'), (1, 'Female'), (2, 'Prefer not to say')], null=True),
        ),
    ]