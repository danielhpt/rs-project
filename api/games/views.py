from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView, Response, status

from .models import Publisher, Game

from .serializer import PublisherSerializer, GameSerializer, PublisherDetailsSerializer, GameDetailsSerializer


class PublishersList(APIView):
    """List all publishers"""

    def get(self, request):
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PublisherDetailsSerializer(data=request.data.copy())

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublisherDetails(APIView):
    """List a publisher"""

    def get(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        serializer = PublisherDetailsSerializer(publisher)

        return Response(serializer.data)


class GamesList(APIView):
    """List all games from a publisher"""

    def get(self, request, publisher_pk):
        publisher = get_object_or_404(Publisher, pk=publisher_pk)
        games = Game.objects.all().filter(publisher=publisher)
        serializer = GameSerializer(games, many=True)

        return Response(serializer.data)

    def post(self, request, publisher_pk):
        publisher = get_object_or_404(Publisher, pk=publisher_pk)
        data = request.data.copy()
        data["publisher"] = publisher.id
        serializer = GameDetailsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, publisher_pk):
        publisher = get_object_or_404(Publisher, pk=publisher_pk)
        games = Game.objects.all().filter(publisher=publisher)
        serializer = GameSerializer(games, many=True)

        for game in games:
            game.delete()

        return Response({})


class GameDetails(APIView):
    """List the details of a Game"""

    def get(self, request, publisher_pk, pk):
        publisher = get_object_or_404(Publisher, pk=publisher_pk)
        game = get_object_or_404(Game, pk=pk, publisher=publisher)
        serializer = GameDetailsSerializer(game)

        return Response(serializer.data)

    def put(self, request, publisher_pk, pk):
        publisher = get_object_or_404(Publisher, pk=publisher_pk)
        game = get_object_or_404(Game, pk=pk, publisher=publisher)
        data = request.data.copy()
        data["publisher"] = publisher.id
        serializer = GameDetailsSerializer(game, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, publisher_pk, pk):
        publisher = get_object_or_404(Publisher, pk=publisher_pk)
        game = get_object_or_404(Game, pk=pk, publisher=publisher)
        serializer = GameDetailsSerializer(game)

        game.delete()

        return Response({})

