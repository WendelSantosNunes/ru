# Generated by Django 4.1 on 2023-02-28 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refeicao', '0006_qtdrefeicao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='decricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='refeicao',
            field=models.IntegerField(choices=[(1, 'Almoço'), (2, 'Almoço Vegetariano'), (3, 'Jantar'), (4, 'Jantar Vegetariano')]),
        ),
    ]