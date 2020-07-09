from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles  import views

router = DefaultRouter()
router.register('viewset', views.HelloViewSet, basename="viewset")
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello/', views.HelloAPIView.as_view(), name="hello"),
    path('', include(router.urls))
]