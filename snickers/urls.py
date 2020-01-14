from django.urls import path
from .views import SnickersPageView

urlpatterns = [
    path('snickers/', SnickersPageView.as_view() , name = 'snickers'),
]
