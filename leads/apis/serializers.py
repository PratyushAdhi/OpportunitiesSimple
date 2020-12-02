from ..models import Language, Lead, Genre, Business
from rest_framework import serializers

class LanguageSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    class Meta:
        model = Language
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    class Meta:
        model = Genre
        fields = "__all__"

class BusinessSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    class Meta:
        model = Business
        fields = "__all__"

class LeadSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=False)
    language_id = LanguageSerializer(many=True, required=False)
    genre_id = GenreSerializer(many=True, required=False)
    business_id = BusinessSerializer(many=True, required=False)


    class Meta:
        model = Lead
        fields = "__all__"
        extra_kwargs = {
            "user": {
                "read_only": True
            },
            'id': {'validators': []},
            "pending_status": {
                "read_only": True
            },
        }


    def create(self, validated_data):
        language_data = validated_data.pop("language_id", None)
        genre_data = validated_data.pop("genre_id", None)
        business_data = validated_data.pop("business_id", None)

        languages = []
        genres = []
        businesses = []
        lead = Lead.objects.create(**validated_data)
        if language_data is not None:
            for language in language_data:
                try:
                    language_obj = Language.objects.get(name=language["name"])
                except:
                    language_obj = Language.objects.create(**language)
                lead.language_id.add(language_obj)

        if genre_data is not None:

            for genre in genre_data:
                try:
                    genre_obj = Genre.objects.get(name=genre["name"])
                except:
                    genre_obj = Genre.objects.create(**genre)
                lead.genre_id.add(genre_obj)

        if business_data is not None:
            for business in business_data:
                try:
                    print("ok")
                    business_obj = Business.objects.filter(name=business["name"])
                    print("ok2")
                    business_obj = business_obj.filter(other=business["other"])
                    print("okay")
                except:
                    business_obj = Business.objects.create(**business)
                lead.business_id.add(business_obj)

        return lead

    def update(self, instance, validated_data):

        language_ids = [item.get("id", None) for item in validated_data['language_id']]

        for language in instance.language_id.all():
            if language.id not in language_ids:
                language.delete()

    # Create or update page instances that are in the request
        for item in validated_data['language_id']:
            if item.get("id", None) is not None:
                lang = Language.objects.get(id=item["id"])
                lang.name = item["name"]
            else:
                try:
                    lang = Language.objects.get(name=item['name'])
                except:
                    lang = Language.objects.create(name=item['name'])
            lang.save()
            instance.language_id.add(lang)

        genre_ids = [item.get("id", None) for item in validated_data['genre_id']]
        for genre in instance.genre_id.all():
            if genre.id not in genre_ids:
                genre.delete()

    # Create or update page instances that are in the request
        for item in validated_data['genre_id']:
            if item.get("id", None) is not None:
                gen = Genre.objects.get(id=item["id"])
                gen.name = item["name"]
            else:
                try:
                    gen = Genre.objects.get(name=item["name"])
                except:
                    gen = Genre.objects.create(**item)
            gen.save()
            instance.genre_id.add(gen)

        business_ids = [item.get("id", None) for item in validated_data['business_id']]
        for business in instance.business_id.all():
            if business.id not in business_ids:
                business.delete()

    #Create or update page instances that are in the request
        for item in validated_data['business_id']:
            if item.get("id", None) is not None:
                bus = Business.objects.get(id=item["id"])
                bus.name = item["name"]
                if item.get("other", None) is not None:
                    bus.other = item["other"]
            else:
                try:
                    bus = Business.objects.get(name=item["name"])
                except:
                    bus = Business.objects.create(**item)
            bus.save()
            instance.business_id.add(bus)

        validated_data.pop("language_id")
        validated_data.pop("business_id")
        validated_data.pop("genre_id")
        [setattr(instance, k, v) for k, v in validated_data.items()]
        instance.save()
        return instance
       