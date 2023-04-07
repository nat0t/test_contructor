from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Subcategory


class CustomModelChoiceIterator(forms.models.ModelChoiceIterator):
    def choice(self, obj):
        return (
            forms.models.ModelChoiceIteratorValue(self.field.prepare_value(obj), obj),
            self.field.label_from_instance(obj),
            obj,
        )


class CustomModelChoiceField(forms.models.ModelMultipleChoiceField):
    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices
        return CustomModelChoiceIterator(self)
    choices = property(_get_choices, forms.MultipleChoiceField._set_choices)


class CreateQuizForm(forms.Form):
    username = forms.CharField(
        label=_('Ф.И.О. тестируемого'),
        widget=forms.TextInput(attrs={'placeholder': 'Ф.И.О.'}),
        error_messages={'required': _('Необходимо ввести имя')},
    )
    subcategories = CustomModelChoiceField(
        queryset=Subcategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label=_('Блоки'),
        error_messages={'required': _('Необходимо выбрать хотя бы один блок.')},
    )


class LoginCreateQuizForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'on'}),
        label=_('Пароль'),
    )
