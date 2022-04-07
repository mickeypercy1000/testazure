from django.urls import path
from product.views import AddProductView, HomepageView

urlpatterns = [
    path('', HomepageView, name = 'home'),
    path('add-products', AddProductView, name = 'add-products'),

]