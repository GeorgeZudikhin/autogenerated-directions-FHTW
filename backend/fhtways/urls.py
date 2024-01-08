from django.urls import path
from .views import PathFindingView

urlpatterns = [
    path('find-path/', PathFindingView.as_view(), name='find-path'),
]
