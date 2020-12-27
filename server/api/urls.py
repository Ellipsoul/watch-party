from django.urls import path
from .views import RoomView

app_name = 'backend'
urlpatterns = [
    path('', RoomView.as_view())
]