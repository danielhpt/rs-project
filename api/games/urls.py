from django.urls import path

from . import views

urlpatterns = [
    path('publishers/', views.PublishersList.as_view(), name="publishers_list"),
    path('publishers/<int:pk>/', views.PublisherDetails.as_view(), name="publisher_detail"),
    path('publishers/<int:publisher_pk>/games/', views.GamesList.as_view(), name="publisher_games"),
    path('publishers/<int:publisher_pk>/games/<int:pk>/', views.GameDetails.as_view(), name="game_detail"),
]
