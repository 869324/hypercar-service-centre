from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render
import random

oil = []
tires = []
diagnostics = []
num = 0
dic = {"ticket": "Waiting for the next client"}


def get_time(idn):
    time = 0
    if idn in oil:
        index = oil.index(idn)
        time = 2 * index
    elif idn in tires:
        index = tires.index(idn)
        time = (len(oil) * 2) + (5 * index)
    else:
        index = diagnostics.index(idn)
        time = (len(oil) * 2) + (5 * len(tires)) + (30 * index)
    cont = {"idn": idn, "time": time}
    return cont


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tickets/menu.html')


class OilView(View):
    def get(self, request, *args, **kwargs):
        global num
        num += 1
        oil.append(num)
        cont = get_time(num)
        return render(request, 'tickets/line.html', context=cont)


class TireView(View):
    def get(self, request, *args, **kwargs):
        global num
        num += 1
        tires.append(num)
        cont = get_time(num)
        return render(request, 'tickets/line.html', context=cont)


class DiagnosticView(View):
    def get(self, request, *args, **kwargs):
        global num
        num += 1
        diagnostics.append(num)
        cont = get_time(num)
        return render(request, 'tickets/line.html', context=cont)


class ProcessView(View):
    def get(self, request, *args, **kwargs):
        queue = {"oil": len(oil), "tires": len(tires), "diag": len(diagnostics)}
        return render(request, "tickets/processing.html", context=queue)

    def post(self, request, *args, **kwargs):
        global dic
        msg = "Waiting for the next client"
        if len(oil) > 0:
            msg = "Next ticket #" + str(oil[0])
            del oil[0]
        elif len(tires) > 0:
            msg = "Next ticket #" + str(tires[0])
            del tires[0]
        elif len(diagnostics) > 0:
            msg = "Next ticket #" + str(diagnostics[0])
            del diagnostics[0]

        dic["ticket"] = msg
        return render(request, "tickets/next.html", context=dic)


class NextView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tickets/next.html", context=dic)

