"""app_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path


from apps import views

urlpatterns = [

    path('', views.some_view, name='some_view'),
    path("project_index", views.project_index, name="project_index"),
    path('sync_charts', views.sync_charts, name='get_name'),
    path('some_view', views.some_view, name='some_view'),

    # path('index', views.process_mongo_db_prom_ql, name='index'),
    # path("<int:pk>/", views.project_detail, name="project_detail"),
    # path('api/users', views.UserCreate.as_view(), name='account-create'),
    # path(r'^users/', include('apps.urls')),
]

