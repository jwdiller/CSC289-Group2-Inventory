# Generated by Django 4.1.7 on 2023-04-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='salesTax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateTimeField(verbose_name='Date and Time')),
            ],
        ),
    ]
