# Alexandria/primer/views.py

from django.http import HttpResponse


def say_hello(request):
    message = 'Hola wey! No se si esta funcionando esto.'

    return HttpResponse(message, content_type='text/plain')
