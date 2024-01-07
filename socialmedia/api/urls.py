from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from user_profile.views import ProfileViewSet
from friends.views import FriendViewSet
from api.views import BlacklistTokenUpdateView
from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns=[
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/blacklist/',BlacklistTokenUpdateView.as_view(),name="blacklist")
]

router = DefaultRouter()
router.register(r'users',UserViewSet,basename='users')
router.register(r'profiles',ProfileViewSet,basename='profiles')
router.register(r'friends',FriendViewSet,basename='friends')
urlpatterns=urlpatterns+router.urls