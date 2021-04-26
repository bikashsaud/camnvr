from django.urls import path
# from home.views import HomeIndexView
from home import views

# from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stream/', views.stream, name="stream" ),
]

