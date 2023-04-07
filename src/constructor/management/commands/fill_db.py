from django.core.management import BaseCommand
from openpyxl.reader.excel import load_workbook

from constructor.models import Question, Answer, Category, Subcategory

FILENAME = 'base.xlsx'
START_ROW = 6
END_ROW = 453


class Command(BaseCommand):
    help = 'Fill database of questions and answers.'

    def handle(self, *args, **options):
        try:
            wb = load_workbook(FILENAME)
            sheet = wb.get_sheet_by_name('Вопросы')
            for i in range(START_ROW, END_ROW + 1):
                # Get or create category.
                category, _ = Category.objects.get_or_create(
                    name=sheet[f'D{i}'].value.strip().capitalize(),
                    defaults={'name': sheet[f'D{i}'].value.strip().capitalize()})
                # Get or create subcategory.
                subcategory, _ = Subcategory.objects.get_or_create(
                    category=category, name=sheet[f'E{i}'].value.strip().capitalize(),
                    defaults={
                        'category': category,
                        'name': sheet[f'E{i}'].value.strip().capitalize(),
                    })
                # Get or create question.
                question, _ = Question.objects.get_or_create(
                    subcategory=subcategory, text=sheet[f'A{i}'].value.strip().capitalize(),
                    defaults={
                        'subcategory': subcategory,
                        'text': sheet[f'A{i}'].value.strip().capitalize(),
                    })
                # Get or create answer.
                answer, _ = Answer.objects.get_or_create(
                    question=question, text=sheet[f'A{i}'].value.strip().capitalize(),
                    defaults={
                        'question': question,
                        'text': sheet[f'B{i}'].value.strip().capitalize(),
                        'is_right': bool(sheet[f'C{i}'].value),
                    },
                )
            self.stdout.write(self.style.SUCCESS(f'Data was imported from the file {FILENAME}.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Error. File with data not found.'))
