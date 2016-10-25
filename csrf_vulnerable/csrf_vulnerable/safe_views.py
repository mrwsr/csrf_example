import os
from django.core.exceptions import SuspiciousOperation
from django.http.response import HttpResponse
from django.template.loader import get_template

CSRF_COOKIE_NAME = 'CSRF_COOKIE'
CSRF_FORM_NAME = 'csrftoken'


def get_csrf_token(request, rotate=False):
    cookie = request.COOKIES.get(CSRF_COOKIE_NAME)
    if rotate or not cookie:
        return os.urandom(32).encode('hex')
    return cookie


def set_csrf_token(response, token):
    response.set_cookie(CSRF_COOKIE_NAME, token)


def check_csrf_token(request):
    cookie = request.COOKIES.get(CSRF_COOKIE_NAME)
    if request.method == "POST":
        if not cookie or cookie != request.POST.get(CSRF_FORM_NAME):
            raise SuspiciousOperation("Bad CSRF token")


def give_amount_to(amount, recipient):
    width = 70
    print " TRANSFER ".center(width, "*")
    print "amount:", amount
    print "recipient:", recipient
    print "*" * width


def transfer(request):
    check_csrf_token(request)

    is_post = request.method == "POST"

    csrf_token = get_csrf_token(request, rotate=is_post)
    context = {CSRF_FORM_NAME: csrf_token}

    if is_post:
        context["amount"] = amount = request.POST.get("amount")
        context["recipient"] = recipient = request.POST.get("recipient")
        give_amount_to(amount, recipient)

    rendered_template = get_template("safe_transfer.html").render(context)

    response = HttpResponse(rendered_template)
    set_csrf_token(response, csrf_token)
    return response
