from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported.")
    return HttpResponse(challenge_text)


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)
