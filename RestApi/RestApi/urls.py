"""RestApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from ServerTreatBox import views
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.start_session_view, name='login'),
    path('register/', views.register, name='register'),
    path('user/<str:username>/', views.user, name='user'),
    path('peliculas/<int:id_solicitado>', views.film_saved_view, name='film_saved_view'),
    path('series/<int:id_solicitado>', views.series_saved_view, name='series_saved_view'),
    path('juegos/<int:id_solicitado>', views.games_saved_view, name='games_saved_view'),
    path('juegos/<int:id_juegos>/favoritos', views.games_insert_view, name='games_insert_view'),
    path('series/<int:id_series>/favoritos', views.series_insert_view, name='series_insert_view'),
    path('peliculas/<int:id_peliculas>/favoritos', views.movie_insert_view, name='movie_insert_view'),






]
