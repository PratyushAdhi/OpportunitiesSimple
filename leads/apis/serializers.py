from ..models import Language, Lead, Genre, Business
from rest_framework import serializers

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"

class LeadSerializer(serializers.ModelSerializer):
    language_id = LanguageSerializer(many=True)
    genre_id = GenreSerializer(many=True)
    business_id = BusinessSerializer(many=True)
    # language_id = serializers.HyperlinkedRelatedField(queryset=Language.objects.all(), many=True,view_name="language-rud")
    # genre_id = serializers.HyperlinkedRelatedField(queryset = Genre.objects.all(), many=True, view_name="genre-rud")
    # business_id = serializers.StringRelatedField(queryset = Business.objects.all(), many=True, view_name="business-rud")
    # language_id = serializers.RelatedField()
    # genre_id = serializers.RelatedField()
    # business_id = serializers.RelatedField()
    class Meta:
        model = Lead
        fields = "__all__"

    def create(self, validated_data):
        language_data = validated_data.pop("language_id")
        genre_data = validated_data.pop("genre_id")
        business_data = validated_data.pop("business_id")

        languages = []
        genres = []
        businesses = []
        lead = Lead.objects.create(**validated_data)

        for language in language_data:
            language_obj = Language.objects.create(**language)
            lead.language_id.add(language_obj)

        for genre in genre_data:
            genre_obj = Genre.objects.create(**genre)
            lead.genre_obj.add(genre_obj)


        for business in business_data:
            business_obj = Business.objects.create(**business)
            lead.business_id.add(business_obj)

        return lead

    def update(self, instance, validated_data):
        language_data = validated_data.pop("language_id")
        genre_data = validated_data.pop("genre_id")
        business_data = validated_data.pop("business_id")
        
        if language_data:
            for language in language_data:
                if language.get("id", None) is not None:
                    lang = Language.objects.get(id=language["id"])
                    if lang:
                        lang.save(**language)
                    else:
                        serializers.ValidationError("No such detail")
                else:
                    lang = Language.objects.create(**language)
                    instance.language_id.add(lang)
        if genre_data:
            for genre in genre_data:
                if genre.get("id", None) is not None:
                    gen = Genre.objects.get(id=genre["id"])
                    if gen:
                        gen.save(**genre)
                    else:
                        serializers.ValidationError("No such genre")
                else:
                    gen = Genre.objects.create(**genre)
                    instance.genre_id.add(gen)
        if business_data:
            for business in business_data:
                if business.get("id", None) is not None:
                    bus = Business.objects.get(id=business["id"])
                    if bus:
                        bus.save(**business)
                    else:
                        serializers.ValidationError("No such business")
                else:
                    bus = Business.objects.create(**business)
                    instance.business_id.add(bus)
        instance.save()
        return instance

