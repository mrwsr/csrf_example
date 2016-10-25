from django.shortcuts import render


def evil_csrf(request):
    return render(request, "evil_csrf.html", context={})


def defeated_csrf(request):
    return render(request, "defeated_csrf.html", context={})
