from django.urls import path
from . import views

urlpatterns = [
    # ex. /polls/
    path("", views.index, name="index"),
    # ex. /polls/5/
    path("<int:questions_id>/", views.detail, name="index"),
    # ex. /polls/5/results
    path("<int:questions_id>/results/", views.results, name="index"),
    # ex. /polls/5/vote
    path("<int:questions_id>/vote/", views.vote, name="index"),
]