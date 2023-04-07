from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('constructor/', include('constructor.urls', namespace='constructor')),
    path('quizzing/', include('quizzing.urls', namespace='quizzing')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
