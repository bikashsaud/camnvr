from django.urls import path

from camnvr.home import views

urlpatterns = [
    path('', views.HomeIndexView.as_view()),
    path('stream/<str:id>', views.stream, name='stream'),
]
