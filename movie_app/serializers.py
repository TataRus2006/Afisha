from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorListSerializers(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

    def get_movies_count(self, obj_director):
        return obj_director.movies.count()


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()


class MovieListSerializers(serializers.ModelSerializer):
    director = DirectorSerializers()

    class Meta:
        model = Movie
        fields = 'title description duration director director_name'.split()


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title'.split()


class ReviewListSerializers(serializers.ModelSerializer):
    movie = MovieSerializers()

    class Meta:
        model = Review
        fields = 'text movie movie_title stars'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id movie text stars'.split()

    def to_representation(self, instance):
        show = super().to_representation(instance)
        show['movie'] = instance.movie.title

        return show


class MoviesReviewsListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title reviews rating'.split()

    def get_rating(self, obj_movie):
        sum_ = 0
        for i in obj_movie.reviews.all():
            sum_ += int(i.stars)
        return round(sum_ / obj_movie.reviews.count(), 1) if obj_movie.reviews.count() else "This movie has no rating"
