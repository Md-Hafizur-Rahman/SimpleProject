from unicodedata import name
from django.contrib import admin
from django.urls import include ,path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tuition/',include('tuition.urls')),
   # path('home/', HomeView.as_view(),name='home')
   #another process 
   path('home/', HomeView.as_view(template_name='home2.html'),name='homeview')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)