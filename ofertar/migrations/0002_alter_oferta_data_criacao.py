# Generated by Django 3.2.5 on 2022-01-24 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='data_criacao',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]