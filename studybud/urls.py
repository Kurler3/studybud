from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # EVERY URL THAT MATCHES AN EMPTY STRING GOES TO THE BASE APP URLS
    path('', include('base.urls'))
]
