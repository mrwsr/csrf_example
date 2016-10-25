import os
from django.shortcuts import render


def give_amount_to(amount, recipient):
    width = 70
    print " TRANSFER ".center(width, "*")
    print "amount:", amount
    print "recipient:", recipient
    print "*" * width


def transfer(request):
    context = {}
    if request.method == "POST":
        context["amount"] = amount = request.POST.get("amount")
        context["recipient"] = recipient = request.POST.get("recipient")
        give_amount_to(amount, recipient)
    return render(request, "transfer.html", context=context)
