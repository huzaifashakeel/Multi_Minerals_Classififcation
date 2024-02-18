from django.urls import path
from .views import MineralView


urlpatterns = [
    path('identify/', MineralView.as_view()),
]