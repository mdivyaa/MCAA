
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phase1/',include('phase1.urls')),
    path('phase2/',include('phase2.urls')),
     path('phase3/',include('phase3.urls')),
   
]
