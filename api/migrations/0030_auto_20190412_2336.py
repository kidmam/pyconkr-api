# Generated by Django 2.2 on 2019-04-12 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20190412_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pyconkorea',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='pyconkorea',
            name='updated_at',
        ),
    ]
