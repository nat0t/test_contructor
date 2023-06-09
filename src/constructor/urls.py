from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'constructor'

urlpatterns = [
    path('delete/<int:quiz_id>/', views.delete_quiz, name='delete_quiz'),
    path('login/', views.login_create_quiz, name='login_create_quiz'),
    path('', views.create_quiz, name='create_quiz'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
