from leads.models import Language, Lead, Genre
from leads.apis.serializers import LeadSerializer, GenreSerializer, LanguageSerializer
from ..models import Detail, Contact
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class DetailSerializer(serializers.ModelSerializer):
    language_id = LanguageSerializer(many=True)
    genre_id = GenreSerializer(many=True)
    contact_1 = ContactSerializer(required=False, allow_null=True)
    contact_2 = ContactSerializer(required=False, allow_null=True)
    class Meta:
        model = Detail
        exclude = ("is_verified",)
        extra_kwargs = {
            'lead': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        language_data = validated_data.pop("language_id")
        genre_data = validated_data.pop("genre_id")
        contact_1 = validated_data.pop("contact_1")
        contact_2 = validated_data.pop("contact_2")
        languages = []
        genres = []
        businesses = []
        detail = Detail.objects.create(**validated_data)

        for language in language_data:
            language_obj = Language.objects.create(**language)
            detail.language_id.add(language_obj)

        for genre in genre_data:
            genre_obj = Genre.objects.create(**genre)
            detail.genre_id.add(genre_obj)

        contact_1 = Contact.objects.create(**contact_1)
        contact_2 = Contact.objects.create(**contact_2)

        detail.contact_1 = contact_1
        detail.contact_2 = contact_2

        detail.save()

        return detail

    def update(self, instance, validated_data):
    
        language_ids = [item.get('id', None) for item in validated_data['language_id']]

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
                    lang = Language.objects.get(name=item["name"])
                except:
                    lang = Language.objects.create(**item)
            lang.save()
            instance.language_id.add(lang)
        validated_data.pop("language_id")

        genre_ids = [item.get('id', None) for item in validated_data['genre_id']]
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

        validated_data.pop("genre_id")

        contact_1 = validated_data.pop("contact_1", None)
        if contact_1 is not None:
            if instance.contact_1 is not None:
                instance.contact_1.name = contact_1["name"]
                instance.contact_1.email = contact_1["email"]
                instance.contact_1.phone_no = contact_1["phone_no"]
            else:
                instance.contact_1 = Contact.objects.create(**contact_1)


        contact_2 = validated_data.pop("contact_2", None)
        if contact_2 is not None:
            if instance.contact_2 is not None:
                print(contact_2["name"])
                instance.contact_2.name = contact_2["name"]
                instance.contact_2.email = contact_2["email"]
                instance.contact_2.phone_no = contact_2["phone_no"]
            else:
                instance.contact_2 = Contact.objects.create(**contact_2)
        [setattr(instance, k, v) for k, v in validated_data.items()]
        instance.save()
        return instance

