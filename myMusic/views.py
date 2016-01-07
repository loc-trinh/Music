from django.shortcuts import render
from django.http import HttpResponse
from youtube import run_query


def index(request):
    context = {}
    if request.method == "POST":
        query = request.POST["query"]
        context["videos"] = run_query(query)
    return render(request, "YTD/index.html", context)