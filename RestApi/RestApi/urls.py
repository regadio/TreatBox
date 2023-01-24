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
    path('sessions/', views.sessions_view, name='sessions'),
<<<<<<< HEAD
    path('peliculas/<int:id_solicitado>', views.film_detail_view, name='detail_view'),
=======
    path('register/', views.register, name='register'),
>>>>>>> c1df2afb9469739bd3f33cb8542155f9d3b0ece2

]
