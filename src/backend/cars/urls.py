from django.urls import path

from cars.views import CarListApi


app_name = 'cars'

urlpatterns = [
    path('', CarListApi.as_view(), name='list'),
]
