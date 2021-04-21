from django.urls import path
from service import camnvr_service
from dashboard.views import DashboardIndexView
from django.conf import settings
from . import views

# service = camnvr_service.CamNVR()
# service.start()
# dashboard = DashboardIndexView()

urlpatterns = [
    path('', DashboardIndexView.as_view(), name=settings.DASHBOARD_URL),
    path('stream/<str:id>', views.stream, name='stream' ),
]