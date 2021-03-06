# Generated by Django 3.2 on 2021-05-09 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210509_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='trades',
        ),
        migrations.AddField(
            model_name='customuser',
            name='trades',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='user_trades_list', to='accounts.Cards'),
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='wants',
        ),
        migrations.AddField(
            model_name='customuser',
            name='wants',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='user_wants_list', to='accounts.Cards'),
        ),
    ]
