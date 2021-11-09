from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:server_type>/', views.get_server_details, name='Cisco_servers'),
    path('create_device/<str:type>',views.create_device,name='create_device'),
    path('signup/', views.signupuser, name='signup'),
    path('login/', views.logging,name='login'),
    path('logout/',views.loggingout,name='loggingout')
]