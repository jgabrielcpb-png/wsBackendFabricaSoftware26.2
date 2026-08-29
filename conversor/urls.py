from django.urls import path, include
from rest_framework import routers
from .views import MoedaViewSet, ConversaoView

router = routers.DefaultRouter()
router.register(r'moedas', MoedaViewSet, basename='moeda')

urlpatterns = [
    path('', include(router.urls)),
    path('converter/', ConversaoView.as_view(), name='converter'),

]