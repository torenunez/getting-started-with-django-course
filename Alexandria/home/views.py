# Alexandria/home/views.py
from django.shortcuts import render


def sample(request):
    data = {
        'books':[
            {
                'title': "Frankenstein",
                'author': "Shelly, Mary",
            },
            {
                'title': "Metamorphosis",
                'author': "Kafka, Franz",
                'recommended': True,
            },
            {
                'title': "Dracula",
                'author': "Stoker, Bram",
                'recommended': False,
            },
        ]

    }

    return render(request, "sample.html", data)