# Generated by Django 3.0.3 on 2020-07-11 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todoitem_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='name',
            field=models.CharField(default='0', max_length=17),
        ),
    ]
