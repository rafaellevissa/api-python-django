# Generated by Django 3.2.7 on 2021-09-16 22:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20210916_0242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='safe_currency_sorce_id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='safe_currency_source_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='currency',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='safe',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='safecurrency',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='safe_currency_received_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
