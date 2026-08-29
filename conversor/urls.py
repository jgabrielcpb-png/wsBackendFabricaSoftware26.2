from django.urls import path, include
from rest_framework import routers
from .views import MoedaViewSet, ConversaoViewSet, ConversaoView

router = routers.DefaultRouter()
router.register(r'moedas', MoedaViewSet, basename='moeda')
router.register(r'conversoes', ConversaoViewSet, basename='conversao')

urlpatterns = [
    path('', include(router.urls)),
    path('converter/', ConversaoView.as_view(), name='converter'),
]
