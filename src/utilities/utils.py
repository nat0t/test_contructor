import smtplib
from logging import getLogger

from django.conf import settings

logger = getLogger('quizzing')


def send_email(username: str, results: list) -> None:
    """Send quiz results to administrator e-mail."""
    try:
        results_text = ''.join([f"{result['subcategory']}: {result['total_right_answered']} / {result['total_questions']}\n" for result in results])
        message = f'Результаты тестирования:\n{results_text}'

        server = smtplib.SMTP(settings.POST_SERVER_NAME, settings.POST_SERVER_PORT)
        server.connect(settings.POST_SERVER_NAME, settings.POST_SERVER_PORT)
        server.sendmail(settings.SERVICE_MAILBOX, settings.ADMINISTRATOR_MAILBOX, message)
        server.quit()
    except Exception as error:
        logger.error('Error while sending e-mail to administrator.', exc_info=error)
