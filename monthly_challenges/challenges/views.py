from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html",
                  {
                      "months": months
                  })

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
        return render(request, "challenges/challenge.html",
                      {
                          "title": month,
                          "h1_text": month,
                          "h2_text": challenge_text
                      })
    except:
        raise Http404()
