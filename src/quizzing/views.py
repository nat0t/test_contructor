import time
from logging import getLogger

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from constructor.forms import LoginCreateQuizForm
from constructor.models import Subcategory
from utilities.utils import send_email
from .models import Quiz, QuizQuestion
from .forms import QuizQuestionForm

logger = getLogger('quizzing')


def select_quiz(request):
    quizzes = Quiz.objects.filter(is_completed=False)
    if request.POST:
        login_form = LoginCreateQuizForm(request.POST)
        if login_form.is_valid():
            if login_form.cleaned_data['password'] == settings.ADMIN_PANEL_PASSWORD:
                time.sleep(2)
                return redirect(reverse('constructor:create_quiz'))
    login_form = LoginCreateQuizForm()
    return render(request, 'quizzing/select_quiz.html', {
        'admin_panel_name': settings.ADMIN_PANEL_NAME,
        'quizzes': quizzes,
        'login_form': login_form,
    })


def pass_quiz(request, quiz_pk):
    if request.method == 'POST':
        form = QuizQuestionForm(request.POST)
        if form.is_valid():
            quiz_question = QuizQuestion.objects.get(pk=form.data['pk'])
            if not form.cleaned_data['answers'].filter(is_right=False):
                quiz_question.is_right_answered = True
            quiz_question.is_answered = True
            quiz_question.save()
        else:
            quiz_question = QuizQuestion.objects.get(pk=form.data['pk'])
            form = QuizQuestionForm(question_pk=quiz_question.question.pk)
            return render(request, 'quizzing/pass_quiz.html', {
                'form': form,
                'pk': quiz_question.pk,
                'subcategory': quiz_question.question.subcategory,
                'text': quiz_question.question.text,
                'error': _('Необходимо выбрать хотя бы один ответ.'),
            })
    else:
        quiz_questions = QuizQuestion.objects.filter(quiz_id=quiz_pk, is_answered=False).order_by('question__subcategory', '?')
        for quiz_question in quiz_questions:
            form = QuizQuestionForm(question_pk=quiz_question.question.pk)
            return render(request, 'quizzing/pass_quiz.html', {
                'form': form,
                'pk': quiz_question.pk,
                'subcategory': quiz_question.question.subcategory,
                'text': quiz_question.question.text,
                })
        # Display quiz results.
        quiz_questions = QuizQuestion.objects.filter(quiz_id=quiz_pk).order_by('question__subcategory', '?')
        subcategories = Subcategory.objects.filter(questions__quizzes=quiz_pk).distinct()
        username = Quiz.objects.get(id=quiz_pk).username
        results = [{
            'subcategory': subcategory,
            'total_questions': quiz_questions.filter(question__subcategory=subcategory).count(),
            'total_right_answered': quiz_questions.filter(question__subcategory=subcategory, is_right_answered=True).count(),
            } for subcategory in subcategories]
        if not Quiz.objects.get(id=quiz_pk).is_completed:
            try:
                send_email(username, results)
            except Exception as error:
                logger.error('Error while sending result of quiz to e-mail', exc_info=error)
        Quiz.objects.filter(id=quiz_pk).update(is_completed=True)
        return render(request, 'quizzing/stop_quiz.html', {
            'total_questions': Quiz.objects.get(id=quiz_pk).questions.count(),
            'total_right_answered': Quiz.objects.get(id=quiz_pk).quiz_questions.filter(is_right_answered=True).count(),
            'username': username,
            'results': results,
        })
    return HttpResponseRedirect(reverse('quizzing:pass_quiz', kwargs={'quiz_pk': quiz_pk}))
