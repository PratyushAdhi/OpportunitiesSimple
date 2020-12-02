from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from .views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups',GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('login/', ObtainAuthToken.as_view(), name="login")
]