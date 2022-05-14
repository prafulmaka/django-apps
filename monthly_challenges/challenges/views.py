from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Sleep for at least 12 hours a day.",
    "february": "Follow Liver King's diet.",
    "march": "Go for a drive everyday.",
    "april": "Stick to a vegan diet.",
    "may": "Stick to a keto diet.",
    "june": "Talk to a stranger every week.",
    "july": "Workout at least 6 times a week.",
    "august": "Read at least 10 pages of a book everyday.",
    "september": "Learn something new every day.",
    "october": "Learn a new programming language and practice it everyday.",
    "november": "Go for a run everyday for at least 15 minutes.",
    "december": "Donate $300."
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")