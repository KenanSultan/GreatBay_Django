from django.urls import path
from .views import *


urlpatterns = [
    path('categories/', Categories.as_view(), name='categories'),
    path('categories/create/', CreateCategory.as_view(), name='create_category'),  
    path('', Products.as_view(), name='products'),  
    path('create/', CreateProduct.as_view(), name='create_product'),
]
