# Generated by Django 3.2 on 2021-05-09 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cards_foreigndata_legalities_meta_rulings_sets_settranslations_tokens'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cards',
        ),
        migrations.DeleteModel(
            name='ForeignData',
        ),
        migrations.DeleteModel(
            name='Legalities',
        ),
        migrations.DeleteModel(
            name='Meta',
        ),
        migrations.DeleteModel(
            name='Rulings',
        ),
        migrations.DeleteModel(
            name='Sets',
        ),
        migrations.DeleteModel(
            name='SetTranslations',
        ),
        migrations.DeleteModel(
            name='Tokens',
        ),
    ]