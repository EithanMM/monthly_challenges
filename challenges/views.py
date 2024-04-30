from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes",
    "march": "Learn Django for at least 20 minutes everyday",
    "april": "april task",
    "may": "may task",
    "june": "JUne task",
    "july": "july task",
    "august": "august task",
    "september": "september task",
    "october": "october task",
    "november": "november task",
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", { "months": months })

# dynamic function that handles months by number
def monthly_challenge_by_number(request, month):
    
    # convert to a list the collection of keys from dictionary
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    # we select the month name by using the month(int) as index of the list
    redirect_month = months[month - 1]
    
    # reverse help us to create a path like '/challenge/january'
    redirect_path = reverse("month-challenge", args=[redirect_month])
    
    return HttpResponseRedirect(redirect_path)

# dynamic function, that holds month dynamic variable
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]        
        return render(request, "challenges/challenge.html", {"text": challenge_text, "month_name": month.capitalize()})
    except:
        raise Http404()