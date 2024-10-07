from django.urls import path
from . import views

urlpatterns = [
    path('<int:room_id>/', views.chat_room, name='chat_room'),
    path('<int:room_id>/send/', views.send_message, name='send_message'),
    path('create/', views.create_room, name='create_room'),
    path('<int:room_id>/add/', views.add_participant, name='add_participant'),
]
