from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [path("<int:pk>", views.RoomDetal.as_view(), name="detail")]
