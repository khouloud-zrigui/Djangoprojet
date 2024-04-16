# Generated by Django 5.0.4 on 2024-04-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_prod', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=100)),
                ('quantite', models.IntegerField()),
                ('prix_unit', models.FloatField()),
            ],
        ),
    ]
