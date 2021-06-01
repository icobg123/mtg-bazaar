from django.contrib.auth import get_user_model
from rest_framework import serializers, validators
# from drf_writable_nested import WritableNestedModelSerializer
# from ..core import models
from .models import *


class CardIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('id',)


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
    # user_id = serializers.IntegerField(required=False)
    password = serializers.CharField(write_only=True)
    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    birth_date = serializers.CharField(required=False)
    depth = 1

    # players = serializers.

    # trades = serializers.Fore
    # trades = serializers.RelatedField(source='core.Cards', read_only=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'password', 'bio', 'gender', 'birth_date', 'trades', 'wants', 'mtg_shops')


class CustomUserRetrieveSerializer(serializers.ModelSerializer):
    birth_date = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    depth = 1

    # user_id = serializers.IntegerField(required=False)

    # trades = serializers.RelatedField(source='core.Cards',  queryset=CustomUser.objects.all())

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'bio', 'gender', 'birth_date', 'id', 'trades', 'wants', 'mtg_shops')


class CustomUserIdRetrieveSerializer(serializers.ModelSerializer):
    # birth_date = serializers.CharField(required=False)
    # bio = serializers.CharField(required=False)
    # gender = serializers.CharField(required=False)
    # depth = 1

    # user_id = serializers.IntegerField(required=False)

    # trades = serializers.RelatedField(source='core.Cards',  queryset=CustomUser.objects.all())

    class Meta:
        model = CustomUser
        fields = ('id',)


class MtgShopSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    lat = serializers.FloatField(required=False)
    long = serializers.FloatField(required=False)
    email = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)  # validators should be a list
    players = CustomUserRetrieveSerializer(read_only=True, many=True)

    class Meta:
        model = MtgShop
        fields = ('name', 'email', 'address', 'lat',
                  'long', 'phone_number', 'players')


class WantsSerializer(serializers.ModelSerializer):
    card = CardIdSerializer(read_only=True)
    # card = serializers.CharField(required=False)
    user = CustomUserIdRetrieveSerializer(required=False)
    count = serializers.IntegerField(required=False)
    depth = 1

    class Meta:
        model = Wants
        fields = ('card', 'user', 'count')


# class TradesSerializer(serializers.ModelSerializer):
#     card = CardIdSerializer(read_only=True)
#     # card = serializers.CharField(required=False)
#     user = CustomUserIdRetrieveSerializer(required=False)
#     count = serializers.IntegerField(required=False)
#     depth = 1
#
#     class Meta:
#         model = Trades
#         fields = ('card', 'user', 'count')


class TradesSerializer(serializers.ModelSerializer):
    card = serializers.PrimaryKeyRelatedField(queryset=Cards.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    # TODO: When updating Trades assign user to currently logged in user

    # card = serializers.IntegerField(source='card.id')
    # user = serializers.IntegerField(source='user.id')

    # card = CardIdSerializer(source='card.id')
    # user = CustomUserIdRetrieveSerializer(source='user.id')

    # def update(self, instance, validated_data):
    #     # trade_data = validated_data.pop('profile')
    #
    #     instance.card = validated_data.get('card', instance.card)
    #     instance.user = validated_data.get('user', instance.card)
    #     instance.save()
    #
    #     # Unless the application properly enforces that this field is
    #     # always set, the following could raise a `DoesNotExist`, which
    #     # would need to be handled.
    #     # profile = instance.profile
    #     #
    #     # instance.username = validated_data.get('username', instance.username)
    #     # instance.email = validated_data.get('email', instance.email)
    #     # instance.save()
    #
    #     # profile.is_premium_member = profile_data.get(
    #     #     'is_premium_member',
    #     #     profile.is_premium_member
    #     # )
    #     # profile.has_support_contract = profile_data.get(
    #     #     'has_support_contract',
    #     #     profile.has_support_contract
    #     # )
    #     # profile.save()
    #
    #     return instance

    class Meta:
        model = Trades

        fields = ('card', 'user', 'count',)
