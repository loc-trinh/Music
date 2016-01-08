from django.shortcuts import render
from youtube import run_query, get_related_videos
from myMusic.models import Playlist, Song
from download import download


def index(request):
    context = {}
    if request.method == "POST":
        query = request.POST["query"]
        context["videos"] = run_query(query)
        context["playlists"] = Playlist.objects.all()
    songs = Song.objects.all()
    if len(songs) > 0:
        context["songs"] = songs
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


def add_to_queue(request):
    if request.method == "GET":
        playlist = Playlist.objects.get(name=request.GET["playlist"])
        song = Song.objects.get_or_create(playlist=playlist, name=request.GET["title"])[0]
        song.url = request.GET["videoId"]
        song.save()
        download(request.GET["videoId"], request.GET["playlist"], request.GET["title"])
        songs = Song.objects.all()
        if len(songs) > 8:
            songs[0].delete()

    return render(request, "YTD/download_queue.html", {"songs": Song.objects.all()})


def about(request):
    return render(request, "YTD/about.html", {})