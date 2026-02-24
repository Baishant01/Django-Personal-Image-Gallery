from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('image_gallery', views.image_gallery_view, name='image_gallery'),
    path('image_details/<int:id>/', views.image_details_view, name='image_details'),
    path('image_delete/<int:id>/', views.image_delete_view, name='image_delete'),
]
