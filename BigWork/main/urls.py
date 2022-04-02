from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('testing', views.testing, name='testing'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('result', views.result, name='result'),
    path('graph', views.graph, name='graph')
]
