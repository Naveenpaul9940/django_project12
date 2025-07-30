from django.contrib import admin
from django.urls import path
from myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registration, name = 'registration'),
    path('login/', login, name = 'login'),
    path('products/',products, name = 'products'),
]
    
