from django.urls import path

from camnvr.home import views

urlpatterns = [
<<<<<<< HEAD:home/urls.py
    path('', HomeIndexView.as_view()),
] 
=======
    path('', views.HomeIndexView.as_view()),
    path('stream/<str:id>', views.stream, name='stream'),
]
>>>>>>> b733f52384d4fdbe8368fd09b82007ddc47da7d7:camnvr/home/urls.py
