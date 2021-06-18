import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PublisherForm, GameForm, GameFormSet
from .models import Publisher, Game
from .serializer import PublisherDetailsSerializer, GameSerializer

url = "http://api:8000/api/"


def index(request):
    return redirect('publishers_list')


def publishersList(request):
    response = requests.get(url + "publishers/").json()

    publishers = []
    for data in response:
        publisher = Publisher(**data)
        publishers.append(publisher)

    context = {
        'publishers': publishers,
        'form': PublisherForm(),
        'formSet': GameFormSet()
    }
    return render(request, 'publishers.html', context=context)


def addPublisher(request):
    form = PublisherForm(request.POST)

    # formset = GameFormSet(request.POST, request.FILES, prefix='games')
    if form.is_valid():  # and formset.is_valid():
        publisher = form.save(commit=False)
        # games = formset.save(commit=False)
        # for game in games:
        #    game.id = 0
        #    game.publisher = publisher
        publisher.id = 0
        pubSerializer = PublisherDetailsSerializer(publisher)
        # gamesSerializer = GameSerializer(games, many=True)
        pubJson = pubSerializer.data
        pubJson['games'] = json.loads(json.dumps([], ensure_ascii=False))
        # pubJson['games'] = json.loads(json.dumps(gamesSerializer.data, ensure_ascii=False))
        response = requests.post(url + 'publishers/', json=pubJson)
        if response.status_code != 201:
            return HttpResponse(status=400)
        return redirect('publishers_list')
    return HttpResponse(status=400)


def delPublisher(request, publisher_pk):
    response = requests.delete(url + "publishers/" + str(publisher_pk) + "/")

    if response.status_code != 200:
        return HttpResponse(status=400)

    return redirect('publishers_list')


def publisherDetails(request, publisher_pk):
    response = requests.get(url + "publishers/" + str(publisher_pk) + "/").json()

    games = response['games']
    del response['games']

    publisher = Publisher(**response)

    context = {
        'publisher': publisher,
        'form': PublisherForm()
    }
    return render(request, 'publisher.html', context=context)


def gamesList(request, publisher_pk):
    response = requests.get(url + "publishers/" + str(publisher_pk) + "/games/").json()

    games = []
    for data in response:
        game = Game(**data)
        games.append(game)

    context = {
        'games': games,
        'publisher_pk': publisher_pk,
        'form': GameForm()
    }
    return render(request, 'games.html', context=context)


def addGame(request, publisher_pk):
    form = GameForm(request.POST)
    if form.is_valid():
        game = form.save(commit=False)
        serializer = GameSerializer(game)
        response = requests.post(url + 'publishers/' + str(publisher_pk) + '/games/', data=serializer.data)
        if response.status_code != 201:
            return HttpResponse(status=400)
        return redirect('publisher_games', publisher_pk=publisher_pk)
    return HttpResponse(status=400)


def delGames(request, publisher_pk):
    response = requests.delete(url + "publishers/" + str(publisher_pk) + "/games/")

    if response.status_code != 200:
        return HttpResponse(status=400)

    return redirect('publisher_detail', publisher_pk=publisher_pk)


def gameDetails(request, publisher_pk, game_pk):
    response = requests.get(url + "publishers/" + str(publisher_pk) + "/games/" + str(game_pk) + "/").json()

    publisher = Publisher(**response['publisher'])
    del response['publisher']
    game = Game(**response, publisher=publisher)

    context = {
        'game': game,
        'publisher_pk': publisher_pk,
        'form': GameForm(initial=response)
    }
    return render(request, 'game.html', context=context)


def editGame(request, publisher_pk, game_pk):
    form = GameForm(request.POST)
    if form.is_valid():
        game = form.save(commit=False)
        serializer = GameSerializer(game)
        response = requests.put(url + 'publishers/' + str(publisher_pk) + "/games/" + str(game_pk) + "/",
                                data=serializer.data)
        if response.status_code != 200:
            return HttpResponse(status=400)
        return redirect('game_detail', publisher_pk=publisher_pk, game_pk=game_pk)
    return HttpResponse(status=400)


def delGame(request, publisher_pk, game_pk):
    response = requests.delete(url + "publishers/" + str(publisher_pk) + "/games/" + str(game_pk) + "/")

    if response.status_code != 200:
        return HttpResponse(status=400)

    return redirect('publisher_games', publisher_pk=publisher_pk)
