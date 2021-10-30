from django.urls import path
from . import views


urlpatterns = [
    path('', views.storeView),
    path('cart/', views.cartView),
    path('cart_add_items/', views.add_cart_items),
    path('cart/del_cart_items_p/', views.del_cart_items )
]




