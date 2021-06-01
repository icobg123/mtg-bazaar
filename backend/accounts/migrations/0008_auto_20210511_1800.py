# Generated by Django 3.2 on 2021-05-11 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_mtgshop_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.cards')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_trades_list', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.cards')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_wants_list', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='trades',
        ),
        migrations.AddField(
            model_name='customuser',
            name='trades',
            field=models.ManyToManyField(blank=True, default='', related_name='user_trades_list', through='accounts.Trades', to='accounts.Cards'),
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='wants',
        ),
        migrations.AddField(
            model_name='customuser',
            name='wants',
            field=models.ManyToManyField(blank=True, default='', related_name='user_wants_list', through='accounts.Wants', to='accounts.Cards'),
        ),
    ]
