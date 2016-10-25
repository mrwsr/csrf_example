from django.shortcuts import render


def evil_csrf(request):
    return render(request, "evil_csrf.html", context={})
