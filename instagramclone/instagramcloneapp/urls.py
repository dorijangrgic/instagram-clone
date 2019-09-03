from django.urls import path
from .views import *

urlpatterns = [
    path('public/', PostListPublic.as_view()),
    path('private/', PostListPrivate.as_view()),
    path('create_post/', PostCreate.as_view())
]
