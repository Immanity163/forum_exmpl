from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from .views import IPREDIRECT

urlpatterns = [
    path('admin/', admin.site.urls , name = 'admin'),
    path('news_feed/',include('News_Feed.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IPREDIRECT)] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)