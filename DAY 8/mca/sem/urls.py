from django.urls import path
from.import views
urlpatterns=[
             path('home/',views.home,name='home'),
             path('mca101/',views.mca101,name='mca101'),
             path('mca102/',views.mca102,name='mca102'),
             path('mca103/',views.mca103,name='mca103'),
             path('mca104/',views.mca104,name='mca104'),
             path('mca105/',views.mca105,name='mca105'),
]