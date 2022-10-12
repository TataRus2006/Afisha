from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class MovieListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title'.split()


class ReviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text'.split()
