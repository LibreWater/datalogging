from django.urls import path
from . import views

app_name = 'myapp'  # Namespace for this app's URLs

urlpatterns = [
    path('runs/', views.RunViewSet.as_view({
        'get': 'list', 
        'post': 'create'}), name='run-list'),
    path('runs/<int:pk>/', views.RunViewSet.as_view({
        'get': 'retrieve', 
        'put': 'update', 
        'delete': 'delete'}), name='run-detail'),
    path('run_data/', views.RunDataViewSet.as_view({
        'get': 'list', 
        'post': 'create'}), name='rundata-list'),
    path('run_data/<int:pk>/', views.RunDataViewSet.as_view({
        'get': 'retrieve', 
        'put': 'update', 
        'delete': 'delete'}), name='rundata-detail'),
]
