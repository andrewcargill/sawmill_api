"""
URL configuration for sawmill_api project.

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
from django.urls import path, include
from lumber.views import TestList, TestDetail, TreeList, TreeDetail, LogList, LogDetail, PlankList, PlankDetail, MoistureCheckList, MoistureDetail
from landing.views import landing_page
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/lumber/', TestList.as_view(), name='lumber-api'),
    path('api/lumber/<int:pk>/', TestDetail.as_view(), name='lumber-detail-api'),
    path('api/tree/', TreeList.as_view(), name='tree'),
    path('api/tree/<int:pk>/', TreeDetail.as_view(), name='tree-detail-api'),
    path('api/log/', LogList.as_view(), name='log'),
    path('api/log/<int:pk>/', LogDetail.as_view(), name='log-detail-api'),
    path('api/plank/', PlankList.as_view(), name='plank'),
    path('api/plank/<int:pk>/', PlankDetail.as_view(), name='plank-detail-api'),
    path('api/water/', MoistureCheckList.as_view(), name='water'),
    path('api/water/<int:pk>/', MoistureDetail.as_view(), name='water-detail-api'),
    path('api-auth/', include('rest_framework.urls')),
     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
     path('api/token/', ObtainAuthToken.as_view(), name='api-token'),
    path('api-auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', landing_page, name='landing_page'),
]

