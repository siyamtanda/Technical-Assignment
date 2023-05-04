"""
URL configuration for myportfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from profiles.admin import custom_admin_site
from .views import user_profile, UserUpdateView, map_view

urlpatterns = [
    path('profile/', user_profile, name='user_profile'),
    path('profile/edit/', UserUpdateView.as_view(success_url=reverse_lazy('user_profile')), name='user_update'),
    path('map/', map_view, name='map_view'),
    path('myadmin/', custom_admin_site.urls),
    path('admin/', admin.site.urls),
]
