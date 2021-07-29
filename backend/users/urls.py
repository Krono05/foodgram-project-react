from django.conf.urls import include
from django.urls import path, re_path

from .views import FollowViewSet, ListFollowViewSet

urlpatterns = [
    path(
        'users/subscriptions/',
        ListFollowViewSet.as_view(),
        name='subscriptions'
    ),
    path('', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    #path('auth/token/login/', obtain_auth_token, name='login'),
    #path('auth/token/logout/', logout, name='logout'),
    path(
        'users/<int:author_id>/subscribe/',
        FollowViewSet.as_view(),
        name='subscribe'
    ),
]
