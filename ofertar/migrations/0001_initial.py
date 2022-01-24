# Generated by Django 3.2.5 on 2022-01-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, null=True)),
                ('valor', models.FloatField(null=True)),
                ('status', models.CharField(choices=[('Destaque', 'Destaque'), ('Aberta', 'Aberta'), ('Fechada', 'Fechada')], max_length=200, null=True)),
            ],
            options={
                'ordering': ['data_criacao'],
            },
        ),
    ]