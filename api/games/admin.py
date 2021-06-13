from django.contrib import admin

from .models import Game, Publisher


class GameInline(admin.TabularInline):
    model = Game


class PublisherAdmin(admin.ModelAdmin):
    inlines = [
        GameInline,
    ]


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Game)
