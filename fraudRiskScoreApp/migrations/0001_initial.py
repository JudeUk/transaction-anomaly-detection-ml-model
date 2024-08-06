# Generated by Django 5.0.3 on 2024-08-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Riskscore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerid', models.CharField(max_length=8)),
                ('accountnumber', models.CharField(max_length=8)),
                ('transactiontype', models.CharField(max_length=6)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('accountbalance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('receivername', models.CharField(max_length=100)),
                ('transactiontime', models.DateTimeField()),
                ('riskscore', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'riskscore',
            },
        ),
    ]
