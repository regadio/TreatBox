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
    path('user/<str:username>/', views.user_data, name='user_data'),
    path('user/edit/<str:username>/', views.user_editdata, name='user_editdata'),
    path('total/<str:username>/', views.total_saved_view, name='total_saved_view'),
    path('peliculas/favoritos/<int:id_pelicula>/', views.movie_insert_view, name='movie_insert_view'),
    path('series/favoritos/<int:id_serie>/', views.serie_insert_view, name='movie_insert_view'),






]
