# Generated by Django 3.1.5 on 2023-04-14 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StockEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_particulars', models.CharField(max_length=50)),
                ('inventory_no', models.CharField(max_length=50)),
                ('rate', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('supplier_name', models.CharField(max_length=50)),
                ('bill_no', models.IntegerField()),
                ('buy_date', models.DateField()),
                ('issued_date', models.DateField()),
                ('head_of_asset', models.CharField(max_length=50)),
                ('section', models.CharField(blank=True, max_length=50, null=True)),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('receiver_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ps2_stocks',
            },
        ),
        migrations.CreateModel(
            name='TransferEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('from_department', models.CharField(max_length=50)),
                ('from_location', models.IntegerField(blank=True, null=True)),
                ('to_department', models.CharField(max_length=50)),
                ('to_location', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField()),
                ('remark', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'ps2_transfer',
            },
        ),
        migrations.CreateModel(
            name='StockAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
