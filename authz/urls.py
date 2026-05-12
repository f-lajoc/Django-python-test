from django.urls import path
from authz.views import SignupView, Loginview, Logoutview

urlpatterns = [  
path('signup', SignupView.as_view(), name='signup'),
path('login', Loginview, name='login'),
path('logout', Logoutview, name='logout'),
]