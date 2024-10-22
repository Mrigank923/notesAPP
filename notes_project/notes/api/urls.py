from django.urls import path
from . import views
from . import auth
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getName),

    path('notes/<str:id>/',views.getNote),
    # Auth URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', auth.register, name='register'),
    path('profile/', auth.get_user_profile, name='user-profile'),

]