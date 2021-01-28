from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('put/', views.put, name='put'),
  path('put/print-label/', views.printscreen, name='printscreen'),
  path('put/auto-search/', views.auto_search, name='auto-search'),
 ]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)