from django.shortcuts import render
from django.http import JsonResponse

from .models import Greeting

# Create your views here.


def index(request):
    return JsonResponse({"random_return": "This is a random return"})


def random_return(request):
    return JsonResponse({
        "price of soda": "1 dollar",
        "price of coca cola": "2 dollars"})

def cake_receipe(request):
    return JsonResponse({
        "cake": {
            "flour": "2 cups",
            "sugar": "1 cup",
            "eggs": "3",
            "butter": "1/2 cup",
            "milk": "1 cup",
            "baking powder": "1 tsp",
            "vanilla extract": "1 tsp"
        },
        "instructions": [
            "Preheat the oven to 350°F (175°C).",
            "In a bowl, mix flour, sugar, baking powder.",
            "Add eggs, butter, milk, and vanilla extract.",
            "Mix until smooth.",
            "Pour into a greased cake pan.",
            "Bake for 30-35 minutes or until golden brown."
        ]
    })

def db(request):
    # If you encounter errors visiting the `/db/` page on the example app, check that:
    #
    # When running the app on Heroku:
    #   1. You have added the Postgres database to your app.
    #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
    #      process entry in `Procfile`, git committed your changes and re-deployed the app.
    #
    # When running the app locally:
    #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
