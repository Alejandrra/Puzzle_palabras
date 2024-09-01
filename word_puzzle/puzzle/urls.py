from django.urls import path
from . import views

urlpatterns = [
    path('<int:puzzle_id>/', views.puzzle_view, name='puzzle_view'),
]
