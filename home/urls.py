from django.urls import path
from . import views
from home.views import HomeIndexView
from django.conf import settings

urlpatterns = [
    path('', HomeIndexView.as_view()),
] 