# Generated by Django 4.1.7 on 2023-04-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0002_subscribe_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='option',
            field=models.CharField(choices=[('W', 'Weekly'), ('M', 'Monthly')], default='M', max_length=2),
        ),
    ]
