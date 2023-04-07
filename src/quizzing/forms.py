from django import forms
from django.utils.translation import gettext_lazy as _

from constructor.models import Answer


class QuizQuestionForm(forms.Form):
    pk = forms.CharField(widget=forms.HiddenInput())
    answers = forms.ModelMultipleChoiceField(
        queryset=Answer.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label=_('Варианты ответов'),
        error_messages={'required': _('Необходимо выбрать хотя бы один ответ.')},
    )

    def __init__(self, *args, **kwargs):
        question_pk = kwargs.pop('question_pk', None)
        super().__init__(*args, **kwargs)
        if question_pk:
            self.fields['answers'].queryset = Answer.objects.filter(question_id=question_pk)
