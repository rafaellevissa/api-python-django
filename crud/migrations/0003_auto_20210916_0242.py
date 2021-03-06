# Generated by Django 3.2.7 on 2021-09-16 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_currency_safe_safecurrency_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='safecurrency',
            name='currency_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='crud_safecurrency', to='crud.currency'),
        ),
        migrations.AddField(
            model_name='safecurrency',
            name='safe_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='crud_safecurrency', to='crud.safe'),
        ),
        migrations.AddField(
            model_name='safecurrency',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='crud_safecurrency', to='crud.user'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='safe',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='safecurrency',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
