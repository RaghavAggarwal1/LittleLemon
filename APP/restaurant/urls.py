# from django.urls import path
# from . import views


# urlpatterns = [
#     path('', views.home, name="home"),
#     path('about/', views.about, name="about"),
#     path('book/', views.book, name="book"),
#     path('reservations/', views.reservations, name="reservations"),
#     path('menu/', views.menu, name="menu"),
#     path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
#     path('bookings', views.bookings, name='bookings'), 
# ]

from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('api-token-auth/', obtain_auth_token)
]