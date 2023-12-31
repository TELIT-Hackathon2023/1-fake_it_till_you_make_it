"""
URL configuration for djangoProject project.

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
from django.contrib import admin
from django.urls import path
from djangoProject.ux import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('receive-string/', views.receive_string, name='receive-string'),
    path('input-form/', views.input_form, name='input_form'),
    path('api/', views.api_view, name='api_view'),
    path('api/chat/', views.api_chat, name='api_chat'),
]