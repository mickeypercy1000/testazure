from django.urls import path
from product.views import AddProductView, HomepageView

urlpatterns = [
    path('', HomepageView, name = 'home'),
    path('add-product', AddProductView, name = 'add-product'),

]