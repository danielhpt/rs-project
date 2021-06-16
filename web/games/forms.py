from django.forms import ModelForm, inlineformset_factory
from .models import Publisher, Game


GameFormSet = inlineformset_factory(Publisher, Game, fields=('title', 'pub_date', 'genre', 'price',))


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'pub_date', 'genre', 'price']
        labels = {
            'pub_date': "Publication Date"
        }
