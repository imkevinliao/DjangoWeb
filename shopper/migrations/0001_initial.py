# Generated by Django 3.2.10 on 2021-12-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(verbose_name='购买数量')),
                ('commodityInfos_id', models.IntegerField(verbose_name='商品ID')),
                ('user_id', models.IntegerField(verbose_name='用户ID')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.CreateModel(
            name='OrderInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]