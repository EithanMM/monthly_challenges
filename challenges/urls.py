from django.urls import path # <- improt 'path' function
from . import views # <- way to import files from the same app

# the dynamic variable 'month' is expected to be dynamic
# and as function parameter, by specifing the value type
# we can filter the view according of the data type of 'month'

# name attr is used to avoid hardcoding url routes and simplify redirections
urlpatterns = [
    path("", views.index, name="index"), # this redirects to 'challenges/'
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]