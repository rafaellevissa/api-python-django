# Generated by Django 3.2.7 on 2021-09-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20210917_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='safecurrency',
            name='safe_id',
        ),
        migrations.AddField(
            model_name='safecurrency',
            name='ammount',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='Safe',
        ),
    ]
