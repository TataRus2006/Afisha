from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorListSerializers, MovieListSerializers, ReviewListSerializers
from .models import Director, Movie, Review


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
