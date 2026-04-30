from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    # is a calculated field
    rate = serializers.SerializerMethodField(read_only=True)

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        return None


    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError("Data de lançamento nao pode ser inferior a 1990.")
        return value
