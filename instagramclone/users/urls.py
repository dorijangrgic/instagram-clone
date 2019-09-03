from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from users.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.obtain_auth_token, name='api-token-auth'),
    path('follow/<int:pk>', FollowView.as_view()),
]