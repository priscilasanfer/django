# Generated by Django 4.0 on 2021-12-22 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_receita_pessoa_alter_receita_date_receita'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='receita',
            name='date_receita',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 12, 22, 17, 36, 27, 545332)),
        ),
    ]
