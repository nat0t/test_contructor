import smtplib
from email.message import EmailMessage
from logging import getLogger

from django.conf import settings

logger = getLogger('quizzing')


def send_email(username: str, results: list) -> None:
    """Send quiz results to administrator e-mail."""
    try:
        results_text = ''.join([f"{result['subcategory']}: {result['total_right_answered']} / {result['total_questions']}\n" for result in results])
        body = f'Результаты тестирования:\n{results_text}'

        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = f'Тестирование: {username}'
        msg['From'] = settings.SERVICE_MAILBOX
        msg['To'] = settings.ADMINISTRATOR_EMAIL

        server = smtplib.SMTP_SSL(settings.POST_SERVER_NAME, settings.POST_SERVER_PORT)
        server.login(settings.SERVICE_MAILBOX, settings.SERVICE_MAILBOX_PASSWORD)
        server.send_message(msg)
        server.quit()
    except Exception as error:
        logger.error('Error while sending e-mail to administrator.', exc_info=error)