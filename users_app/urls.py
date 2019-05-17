from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('logout/', logout_view, name='logout'),
    path('signup/', registration, name='signup'),
    path('login/', login_view, name='login'),
]
