from django.urls import path

from news.views import home, tabiat, jadval, kurs, harif, elon, malumot, animation, efect, animation2

urlpatterns = [
    path('', home),
    path('tabiat/', tabiat),
    path('jadval/', jadval),
    path('kurs/', kurs),
    path("o'zgartirish/", harif),
    path("e'lon/", elon),
    path("ma'lumot/", malumot),
    path("animation/", animation),
    path("efect/", efect),
    path('animation2/', animation2),
]

