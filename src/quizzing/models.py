from django.db import models
from django.utils.translation import gettext_lazy as _


class Quiz(models.Model):
    """Model for keeping quiz."""
    username = models.CharField(max_length=255, verbose_name=_('Ф.И.О. проверяемого'))
    questions = models.ManyToManyField(
        'constructor.Question',
        through='quizzing.QuizQuestion',
        related_name='quizzes',
        verbose_name=_('вопросы'),
    )
    is_completed = models.BooleanField(default=False, verbose_name=_('опрос пройден?'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('опрос')
        verbose_name_plural = _('опросы')


class QuizQuestion(models.Model):
    """Model for keeping info about question of quizz."""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_questions', verbose_name=_('опрос'))
    question = models.ForeignKey('constructor.Question', on_delete=models.CASCADE, related_name='quiz_questions', verbose_name=_('опрос'))
    is_answered = models.BooleanField(default=False, verbose_name=_('на вопрос дан ответ?'))
    is_right_answered = models.BooleanField(default=False, verbose_name=_('на вопрос дан верный ответ?'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quiz.username} | #{self.quiz.pk}'

    class Meta:
        verbose_name = _('вопрос в опросе')
        verbose_name_plural = _('вопросы в опросах')
