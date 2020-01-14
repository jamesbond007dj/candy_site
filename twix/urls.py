from django.urls import path
from .views import TwixPageView

urlpatterns = [

    path('twix/', TwixPageView.as_view() , name = 'twix'),
]
