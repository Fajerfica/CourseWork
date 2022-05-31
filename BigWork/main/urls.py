from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('testing', views.testing, name='testing'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('params', views.params, name='params'),
    path('result', views.result, name='result'),
    path('graph', views.graph, name='graph'),
    path('history', views.history, name='history'),
    path('outsavings', views.outsavings, name='outsavings')
]
