from django.contrib.auth import get_user_model
from rest_framework import serializers, validators
# from ..core import models
from .models import *


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = (
            "id",
            "artist",
            "asciiname",
            "availability",
            "bordercolor",
            "cardkingdomfoilid",
            "cardkingdomid",
            "coloridentity",
            "colorindicator",
            "colors",
            "convertedmanacost",
            "dueldeck",
            "edhrecrank",
            "faceconvertedmanacost",
            "facename",
            "flavorname",
            "flavortext",
            "frameeffects",
            "frameversion",
            "hand",
            "hasalternativedecklimit",
            "hascontentwarning",
            "hasfoil",
            "hasnonfoil",
            "isalternative",
            "isfullart",
            "isonlineonly",
            "isoversized",
            "ispromo",
            "isreprint",
            "isreserved",
            "isstarter",
            "isstoryspotlight",
            "istextless",
            "istimeshifted",
            "keywords",
            "layout",
            "leadershipskills",
            "life",
            "loyalty",
            "manacost",
            "mcmid",
            "mcmmetaid",
            "mtgarenaid",
            "mtgjsonv4id",
            "mtgofoilid",
            "mtgoid",
            "multiverseid",
            "name",
            "number",
            "originalreleasedate",
            "originaltext",
            "originaltype",
            "otherfaceids",
            "power",
            "printings",
            "promotypes",
            "purchaseurls",
            "rarity",
            "scryfallid",
            "scryfallillustrationid",
            "scryfalloracleid",
            "setcode",
            "side",
            "subtypes",
            "supertypes",
            "tcgplayerproductid",
            "text",
            "toughness",
            "type",
            "types",
            "uuid",
            "variations",
            "watermark",
        )


CustomUser = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        write_only=True, validators=[validators.UniqueValidator(
            message='This email already exists',
            queryset=CustomUser.objects.all()
        )]
    )
    password = serializers.CharField(write_only=True)
    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    birth_date = serializers.CharField(required=False)

    # trades = serializers.Fore
    # trades = serializers.RelatedField(source='core.Cards', read_only=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'password', 'bio', 'gender', 'birth_date', 'trades', 'wants')


class CustomUserRetrieveSerializer(serializers.ModelSerializer):
    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)

    # trades = serializers.RelatedField(source='core.Cards',  queryset=CustomUser.objects.all())

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'bio', 'gender', 'birth_date', 'id', 'trades', 'wants')
