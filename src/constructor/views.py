from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from quizzing.models import Quiz
from .forms import CreateQuizForm, LoginCreateQuizForm
from .models import Question


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
    return render(request, 'constructor/create_quiz.html', {
        'form': form,
        'quizzes': Quiz.objects.values_list('pk', 'username'),
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
