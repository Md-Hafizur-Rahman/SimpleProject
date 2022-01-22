from os import name
from django.urls import path
from .views import home ,Postview,postcreate,Subview,ContactFormView
from .forms import ContactFormtwo


urlpatterns = [
    # path('home/',home,name="home"),
    path('showpost/',Postview,name='post'),
    path('create/',postcreate,name='create'),
    path('subshow/',Subview,name='sub'),
    path('contact/',ContactFormView.as_view(),name='sub'),
    path('contact2/',ContactFormView.as_view(form_class=ContactFormtwo,template_name='contact.html'),name='sub'),
]