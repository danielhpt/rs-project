from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('publishers/', views.publishersList, name="publishers_list"),
    path('add_publisher/', views.addPublisher, name="add_publisher"),
    path('del_publisher/<int:publisher_pk>/', views.delPublisher, name="del_publisher"),
    path('publishers/<int:publisher_pk>/', views.publisherDetails, name="publisher_detail"),
    path('publishers/<int:publisher_pk>/games/', views.gamesList, name="publisher_games"),
    path('publishers/<int:publisher_pk>/del_games/', views.delGames, name="del_games"),
    path('publishers/<int:publisher_pk>/add_game/', views.addGame, name="add_game"),
    path('publishers/<int:publisher_pk>/games/<int:game_pk>/', views.gameDetails, name="game_detail"),
    path('publishers/<int:publisher_pk>/edit_game/<int:game_pk>/', views.editGame, name="edit_game"),
    path('publishers/<int:publisher_pk>/del_game/<int:game_pk>/', views.delGame, name="del_game"),
]