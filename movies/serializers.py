from rest_framework import serializers
from movies.models import Movie
from reviews.models import Review
from genres.serializers import GenreSerializer
from actors.serializers import ActorsSerializer
from django.db.models import Sum, Avg


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)  # adiciona o campo 'rate' somente no response da requisição

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        print(rate)
        if rate:
            return round(rate, 1)
        else:
            return None
        # print(obj.title)
        # reviews = obj.reviews.all()
        # sum_reviews = 0
        # if reviews:
        #    for review in reviews:
        #        sum_reviews += review.stars
        #
        #    review_count = reviews.count()
        #    return round(sum_reviews / review_count,1)
        # return None

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    actors = ActorsSerializer(many=True)
    rate = serializers.SerializerMethodField(read_only=True)  # adiciona o campo 'rate' somente no response da requisição

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        print(rate)
        if rate:
            return round(rate, 1)
        else:
            return None

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')
        return value


class MovieStatsSerializers(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
