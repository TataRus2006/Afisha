from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from rest_framework import status
from .serializers import DirectorListSerializers, MovieListSerializers, ReviewListSerializers, \
    MoviesReviewsListSerializer


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    data = DirectorListSerializers(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    data = MovieListSerializers(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def reviews_view(request):
    reviews = Review.objects.all()
    data = ReviewListSerializers(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movies_reviews_view(request):
    movies_reviews = Movie.objects.all()
    data = MoviesReviewsListSerializer(movies_reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_item_view(reques, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Director not found'})
    serializer = DirectorListSerializers(director)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_item_view(reques, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Movie not found'})
    serializer = MovieListSerializers(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_item_view(reques, id):
    try:
        movie = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Review not found'})
    serializer = ReviewListSerializers(movie)
    return Response(data=serializer.data)

