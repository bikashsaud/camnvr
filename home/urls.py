from django.urls import path
from home.views import HomeIndexView

# from home import views

urlpatterns = [
    path('', HomeIndexView.as_view(), name='index'),
]

