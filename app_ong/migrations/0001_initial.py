# Generated by Django 3.2.2 on 2021-05-09 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('nombre', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('annos', models.IntegerField()),
            ],
        ),
    ]