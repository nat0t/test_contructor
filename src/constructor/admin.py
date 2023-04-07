from django.contrib import admin

from .models import Question, Answer, Category, Subcategory


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('text', 'subcategory')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    fields = ('question', 'text', 'is_right')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount')
    fields = ('name', 'category', 'amount')
