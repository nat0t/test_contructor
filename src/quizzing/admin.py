from django.contrib import admin

from .models import Quiz, QuizQuestion


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('username', 'updated_at', 'is_completed')
    fields = ('username', 'is_completed', 'questions')
    readonly_fields = ('questions',)


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    fields = ('quiz', 'question')
