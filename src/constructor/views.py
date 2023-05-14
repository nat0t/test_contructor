from itertools import groupby

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from quizzing.models import Quiz
from .forms import CreateQuizForm, LoginCreateQuizForm
from .models import Question, Category


def create_quiz(request):
    if request.method == 'POST':
        form = CreateQuizForm(request.POST)
        if form.is_valid():
            quiz = Quiz.objects.create(username=form.cleaned_data['username'])
            for subcategory in form.cleaned_data['subcategories']:
                amount = int(request.POST[f'amount_{subcategory.pk}'])
                quiz.questions.add(*Question.objects.filter(subcategory=subcategory)[:amount])
            return HttpResponseRedirect(reverse('constructor:create_quiz'))
    else:
        form = CreateQuizForm()
    quizzes = Quiz.objects.values('pk', 'username', 'created_at')
    for quiz in quizzes:
        quiz['categories'] = [category for category in Category.objects.filter(
            subcategories__questions__quizzes__pk=quiz['pk']).distinct().values_list('name', flat=True)]
        quiz['created_at'] = quiz['created_at'].strftime('%Y.%m.%d')
    quizzes = [(k, list(g)) for k, g in groupby(quizzes, key=lambda x: x['created_at'])]
    return render(request, 'constructor/create_quiz.html', {
        'form': form,
        'quizzes': quizzes,
    })


def delete_quiz(request, quiz_id: None):
    Quiz.objects.filter(pk=quiz_id).delete()
    return HttpResponseRedirect(reverse('constructor:create_quiz'))


def login_create_quiz(request):
    if request.method == 'POST':
        form = LoginCreateQuizForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = LoginCreateQuizForm()
    return render(request, 'constructor/login_create_quiz.html', {'form': form})
