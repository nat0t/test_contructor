from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """Model for keeping category of question."""
    name = models.CharField(max_length=255, verbose_name=_('название'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('блок')
        verbose_name_plural = _('блоки')


class Subcategory(models.Model):
    """Model for keeping subcategory of question."""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name=_('блок'),
    )
    name = models.CharField(max_length=255, verbose_name=_('название'))
    amount = models.PositiveSmallIntegerField(default=10, verbose_name=_('количество вопросов в подкатегории'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('подблок')
        verbose_name_plural = _('подблоки')


class Question(models.Model):
    """Model for keeping test question."""
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name=_('подблок'),
    )
    text = models.TextField(verbose_name=_('содержание вопроса'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('вопрос')
        verbose_name_plural = _('вопросы')


class Answer(models.Model):
    """Model for keeping answer for test question."""
    text = models.TextField(verbose_name=_('содержание ответа'))
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name=_('вопрос'))
    is_right = models.BooleanField(default=False, verbose_name=_('ответ верен?'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('question',)
        verbose_name = _('ответ')
        verbose_name_plural = _('ответы')
