# Generated by Django 4.1 on 2022-08-13 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(blank=True, default='', max_length=400)),
                ('criacao', models.TimeField(auto_now_add=True)),
                ('categoria', models.CharField(blank=True, default='importante', max_length=25)),
                ('status', models.CharField(blank=True, default='Pendente', max_length=25)),
            ],
        ),
    ]