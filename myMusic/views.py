from django.shortcuts import render
from django.http import HttpResponse
from youtube import run_query, get_related_videos


def index(request):
    context = {}
    if request.method == "POST":
        query = request.POST["query"]
        context["videos"] = run_query(query)
    return render(request, "YTD/index.html", context)


def player(request):
    context = {}
    if request.method == "GET":
        context["videoId"] = request.GET["videoId"]
    return render(request, "YTD/player.html", context)


def related_videos(request):
    context = {}
    if request.method == "GET":
        context["videos"] = get_related_videos(request.GET["videoId"])
    return render(request, "YTD/related.html", context)
