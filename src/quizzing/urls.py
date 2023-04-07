from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'quizzing'

urlpatterns = [
    path('pass/<int:quiz_pk>/<int:question_pk>/', views.pass_quiz, name='pass_quiz'),
    path('pass/<int:quiz_pk>/', views.pass_quiz, name='pass_quiz'),
    path('', views.select_quiz, name='select_quiz'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
