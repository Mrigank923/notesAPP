from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.notes_list, name='notes_list'),
    path('note/new/', views.create_note, name='create_note'),
    path('note/<int:pk>/edit/', views.update_note, name='update_note'),
    path('note/<int:pk>/delete/', views.delete_note, name='delete_note'),
]