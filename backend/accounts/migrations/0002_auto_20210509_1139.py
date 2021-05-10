# Generated by Django 3.2 on 2021-05-09 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.TextField(blank=True, null=True)),
                ('asciiname', models.TextField(blank=True, db_column='asciiName', null=True)),
                ('availability', models.TextField(blank=True, null=True)),
                ('bordercolor', models.TextField(blank=True, db_column='borderColor', null=True)),
                ('cardkingdomfoilid', models.TextField(blank=True, db_column='cardKingdomFoilId', null=True)),
                ('cardkingdomid', models.TextField(blank=True, db_column='cardKingdomId', null=True)),
                ('coloridentity', models.TextField(blank=True, db_column='colorIdentity', null=True)),
                ('colorindicator', models.TextField(blank=True, db_column='colorIndicator', null=True)),
                ('colors', models.TextField(blank=True, null=True)),
                ('convertedmanacost', models.TextField(blank=True, db_column='convertedManaCost', null=True)),
                ('dueldeck', models.TextField(blank=True, db_column='duelDeck', null=True)),
                ('edhrecrank', models.IntegerField(blank=True, db_column='edhrecRank', null=True)),
                ('faceconvertedmanacost', models.TextField(blank=True, db_column='faceConvertedManaCost', null=True)),
                ('facename', models.TextField(blank=True, db_column='faceName', null=True)),
                ('flavorname', models.TextField(blank=True, db_column='flavorName', null=True)),
                ('flavortext', models.TextField(blank=True, db_column='flavorText', null=True)),
                ('frameeffects', models.TextField(blank=True, db_column='frameEffects', null=True)),
                ('frameversion', models.TextField(blank=True, db_column='frameVersion', null=True)),
                ('hand', models.TextField(blank=True, null=True)),
                ('hasalternativedecklimit', models.IntegerField(db_column='hasAlternativeDeckLimit')),
                ('hascontentwarning', models.IntegerField(db_column='hasContentWarning')),
                ('hasfoil', models.IntegerField(db_column='hasFoil')),
                ('hasnonfoil', models.IntegerField(db_column='hasNonFoil')),
                ('isalternative', models.IntegerField(db_column='isAlternative')),
                ('isfullart', models.IntegerField(db_column='isFullArt')),
                ('isonlineonly', models.IntegerField(db_column='isOnlineOnly')),
                ('isoversized', models.IntegerField(db_column='isOversized')),
                ('ispromo', models.IntegerField(db_column='isPromo')),
                ('isreprint', models.IntegerField(db_column='isReprint')),
                ('isreserved', models.IntegerField(db_column='isReserved')),
                ('isstarter', models.IntegerField(db_column='isStarter')),
                ('isstoryspotlight', models.IntegerField(db_column='isStorySpotlight')),
                ('istextless', models.IntegerField(db_column='isTextless')),
                ('istimeshifted', models.IntegerField(db_column='isTimeshifted')),
                ('keywords', models.TextField(blank=True, null=True)),
                ('layout', models.TextField(blank=True, null=True)),
                ('leadershipskills', models.TextField(blank=True, db_column='leadershipSkills', null=True)),
                ('life', models.TextField(blank=True, null=True)),
                ('loyalty', models.TextField(blank=True, null=True)),
                ('manacost', models.TextField(blank=True, db_column='manaCost', null=True)),
                ('mcmid', models.TextField(blank=True, db_column='mcmId', null=True)),
                ('mcmmetaid', models.TextField(blank=True, db_column='mcmMetaId', null=True)),
                ('mtgarenaid', models.TextField(blank=True, db_column='mtgArenaId', null=True)),
                ('mtgjsonv4id', models.TextField(blank=True, db_column='mtgjsonV4Id', null=True)),
                ('mtgofoilid', models.TextField(blank=True, db_column='mtgoFoilId', null=True)),
                ('mtgoid', models.TextField(blank=True, db_column='mtgoId', null=True)),
                ('multiverseid', models.TextField(blank=True, db_column='multiverseId', null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('number', models.TextField(blank=True, null=True)),
                ('originalreleasedate', models.TextField(blank=True, db_column='originalReleaseDate', null=True)),
                ('originaltext', models.TextField(blank=True, db_column='originalText', null=True)),
                ('originaltype', models.TextField(blank=True, db_column='originalType', null=True)),
                ('otherfaceids', models.TextField(blank=True, db_column='otherFaceIds', null=True)),
                ('power', models.TextField(blank=True, null=True)),
                ('printings', models.TextField(blank=True, null=True)),
                ('promotypes', models.TextField(blank=True, db_column='promoTypes', null=True)),
                ('purchaseurls', models.TextField(blank=True, db_column='purchaseUrls', null=True)),
                ('rarity', models.TextField(blank=True, null=True)),
                ('scryfallid', models.TextField(blank=True, db_column='scryfallId', null=True)),
                ('scryfallillustrationid', models.TextField(blank=True, db_column='scryfallIllustrationId', null=True)),
                ('scryfalloracleid', models.TextField(blank=True, db_column='scryfallOracleId', null=True)),
                ('setcode', models.TextField(blank=True, db_column='setCode', null=True)),
                ('side', models.TextField(blank=True, null=True)),
                ('subtypes', models.TextField(blank=True, null=True)),
                ('supertypes', models.TextField(blank=True, null=True)),
                ('tcgplayerproductid', models.TextField(blank=True, db_column='tcgplayerProductId', null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('toughness', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('types', models.TextField(blank=True, null=True)),
                ('uuid', models.TextField(unique=True)),
                ('variations', models.TextField(blank=True, null=True)),
                ('watermark', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ForeignData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavortext', models.TextField(blank=True, db_column='flavorText', null=True)),
                ('language', models.TextField(blank=True, null=True)),
                ('multiverseid', models.IntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'foreign_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Legalities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'legalities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('version', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'meta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rulings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rulings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basesetsize', models.IntegerField(blank=True, db_column='baseSetSize', null=True)),
                ('block', models.TextField(blank=True, null=True)),
                ('booster', models.TextField(blank=True, null=True)),
                ('code', models.TextField(unique=True)),
                ('isfoilonly', models.IntegerField(db_column='isFoilOnly')),
                ('isforeignonly', models.IntegerField(db_column='isForeignOnly')),
                ('isnonfoilonly', models.IntegerField(db_column='isNonFoilOnly')),
                ('isonlineonly', models.IntegerField(db_column='isOnlineOnly')),
                ('keyrunecode', models.TextField(blank=True, db_column='keyruneCode', null=True)),
                ('mcmid', models.IntegerField(blank=True, db_column='mcmId', null=True)),
                ('mcmidextras', models.IntegerField(blank=True, db_column='mcmIdExtras', null=True)),
                ('mcmname', models.TextField(blank=True, db_column='mcmName', null=True)),
                ('mtgocode', models.TextField(blank=True, db_column='mtgoCode', null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('parentcode', models.TextField(blank=True, db_column='parentCode', null=True)),
                ('releasedate', models.DateField(blank=True, db_column='releaseDate', null=True)),
                ('sealedproduct', models.TextField(blank=True, db_column='sealedProduct', null=True)),
                ('tcgplayergroupid', models.IntegerField(blank=True, db_column='tcgplayerGroupId', null=True)),
                ('totalsetsize', models.IntegerField(blank=True, db_column='totalSetSize', null=True)),
                ('type', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sets',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SetTranslations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.TextField(blank=True, null=True)),
                ('translation', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'set_translations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.TextField(blank=True, null=True)),
                ('asciiname', models.TextField(blank=True, db_column='asciiName', null=True)),
                ('availability', models.TextField(blank=True, null=True)),
                ('bordercolor', models.TextField(blank=True, db_column='borderColor', null=True)),
                ('coloridentity', models.TextField(blank=True, db_column='colorIdentity', null=True)),
                ('colors', models.TextField(blank=True, null=True)),
                ('edhrecrank', models.IntegerField(blank=True, db_column='edhrecRank', null=True)),
                ('facename', models.TextField(blank=True, db_column='faceName', null=True)),
                ('flavortext', models.TextField(blank=True, db_column='flavorText', null=True)),
                ('frameeffects', models.TextField(blank=True, db_column='frameEffects', null=True)),
                ('frameversion', models.TextField(blank=True, db_column='frameVersion', null=True)),
                ('hasfoil', models.IntegerField(db_column='hasFoil')),
                ('hasnonfoil', models.IntegerField(db_column='hasNonFoil')),
                ('isfullart', models.IntegerField(db_column='isFullArt')),
                ('ispromo', models.IntegerField(db_column='isPromo')),
                ('isreprint', models.IntegerField(db_column='isReprint')),
                ('keywords', models.TextField(blank=True, null=True)),
                ('layout', models.TextField(blank=True, null=True)),
                ('mcmid', models.TextField(blank=True, db_column='mcmId', null=True)),
                ('mtgarenaid', models.TextField(blank=True, db_column='mtgArenaId', null=True)),
                ('mtgjsonv4id', models.TextField(blank=True, db_column='mtgjsonV4Id', null=True)),
                ('multiverseid', models.TextField(blank=True, db_column='multiverseId', null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('number', models.TextField(blank=True, null=True)),
                ('originaltext', models.TextField(blank=True, db_column='originalText', null=True)),
                ('originaltype', models.TextField(blank=True, db_column='originalType', null=True)),
                ('power', models.TextField(blank=True, null=True)),
                ('promotypes', models.TextField(blank=True, db_column='promoTypes', null=True)),
                ('reverserelated', models.TextField(blank=True, db_column='reverseRelated', null=True)),
                ('scryfallid', models.TextField(blank=True, db_column='scryfallId', null=True)),
                ('scryfallillustrationid', models.TextField(blank=True, db_column='scryfallIllustrationId', null=True)),
                ('scryfalloracleid', models.TextField(blank=True, db_column='scryfallOracleId', null=True)),
                ('setcode', models.TextField(blank=True, db_column='setCode', null=True)),
                ('side', models.TextField(blank=True, null=True)),
                ('subtypes', models.TextField(blank=True, null=True)),
                ('supertypes', models.TextField(blank=True, null=True)),
                ('tcgplayerproductid', models.TextField(blank=True, db_column='tcgplayerProductId', null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('toughness', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('types', models.TextField(blank=True, null=True)),
                ('uuid', models.TextField()),
                ('watermark', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tokens',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='trades',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_trades_list', to='accounts.cards'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='wants',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_wants_list', to='accounts.cards'),
        ),
    ]
