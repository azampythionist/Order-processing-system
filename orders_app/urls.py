from django.urls import path
from .views import HomeView, OrderCreateView, OrderItemCreateView, OrderTotalView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('orders', OrderCreateView.as_view(), name='create-order'),
    path('orders/<int:id>/items', OrderItemCreateView.as_view(), name='create-order-item'),
    path('orders/<int:id>/total', OrderTotalView.as_view(), name='order-total'),
]
