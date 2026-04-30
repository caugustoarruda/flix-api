from rest_framework import serializers
from movies.models import Movie
from reviews.models import Review


class MovieSerializer(serializers.ModelSerializer):
    # is a calculated field
    rate = serializers.SerializerMethodField(read_only=True)

    def get_rate(self, obj):
        reviews = obj.reviews.all()

        stars_ = 0
        for review in reviews:
            stars_ += review.stars
        return stars_/len(reviews)

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError("Data de lançamento nao pode ser inferior a 1990.")
        return value
