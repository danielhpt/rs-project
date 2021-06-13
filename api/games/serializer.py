from rest_framework.serializers import ModelSerializer, IntegerField

from .models import Publisher, Game


class GameSerializer(ModelSerializer):
    id = IntegerField()

    class Meta:
        model = Game
        fields = ['id', 'title', 'pub_date', 'genre', 'price']


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'city', 'country', 'website']


class GameDetailsSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'pub_date', 'genre', 'price', 'publisher']

    def to_representation(self, instance):
        self.fields['publisher'] = PublisherSerializer(read_only=True)
        return super(GameDetailsSerializer, self).to_representation(instance)


class PublisherDetailsSerializer(ModelSerializer):
    games = GameSerializer(many=True)

    class Meta:
        model = Publisher
        fields = ['id', 'name', 'city', 'country', 'website', 'games']

    def create(self, validated_data):
        games_data = validated_data.pop('games')
        publisher = Publisher.objects.create(**validated_data)
        for game_data in games_data:
            del game_data['id']
            game = Game(**game_data)
            game.publisher = publisher
            game.save()
        return publisher

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.website = validated_data.get('website', instance.website)
        instance.gameList = validated_data.get('games', instance.games)

        for game_data in validated_data.pop('games'):
            game = instance.games.get(pk=game_data['id'])
            game.title = game_data['title']
            game.pub_date = game_data['pub_date']
            game.genre = game_data['genre']
            game.price = game_data['price']
            game.save()

        return instance
