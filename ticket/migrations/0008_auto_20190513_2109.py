# Generated by Django 2.2 on 2019-05-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_auto_20190513_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('ready', 'ready'), ('paid', 'paid'), ('delete', 'deleted'), ('cancelled', 'cancelled')], default='ready', max_length=10),
        ),
    ]
