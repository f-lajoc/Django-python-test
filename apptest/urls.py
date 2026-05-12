from django.urls import path
from apptest.views import homepage, aboutpage, contactpage, testimonialpage, ContactView

urlpatterns = [  
path('', homepage, name='home'),
path('about', aboutpage, name='about'),
# function based views
# path('contact', contactpage, name='contact'),
# class based views
path('contact', ContactView.as_view(), name='contact'),
path('testimony', testimonialpage, name='testimony'),
]