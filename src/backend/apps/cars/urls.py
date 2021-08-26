from django.urls import path

from apps.cars.views import CarListApi

app_name = 'cars'

urlpatterns = [
    path('', CarListApi.as_view(), name='list'),
]
