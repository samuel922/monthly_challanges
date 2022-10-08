from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "Eat o meat for one month",
    "february": "Go to the gym for at least 45 min everyday",
    "march": "Play soccer for my school to boost our points",
    "april": "Learn to code for 4 hours daily",
    "may": "Attend coding bootcamps twice every week",
    "june": "Meditate for 30 min daily",
    "july": "Practice paidaLajin daily",
    "august": "Eat o meat for one month",
    "september": "Go to the gym for at least 45 min everyday",
    "octobar": "Play soccer for my school to boost our points",
    "november": "Learn to code for 4 hours daily",
    "december": "Attend coding bootcamps twice every week"

}

# Create your views here.

def index(request):
    return HttpResponse("This works")

def mothly_challenge_by_month(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):

    challenge_txt = None

    try:
        challenge_txt = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month challenge does not exist")
    else:
        return HttpResponse(challenge_txt)

    