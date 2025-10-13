from django.shortcuts import  get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Anime, Character

def index(request):
    anime_list = Anime.objects.all()
    context = {"anime_list": anime_list}
    return render(request, "animepage/index.html", context)

def info(request, anime_id):
    info = get_object_or_404(Anime, pk=anime_id)
    return render(request, "animepage/info.html", {"info": info})

def character(request, anime_id, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, "animepage/character.html", {"character": character})

def editCharacter(request, anime_id ,character_id):
    character = get_object_or_404(Character, pk=character_id)

    if request.method == "POST":
        character.name = request.POST.get("name")
        character.age = request.POST.get("age")
        character.description = request.POST.get("description")
        character.save()
        return redirect("anime:character", anime_id=anime_id, character_id=character_id)

    return render(request,  "animepage/editCharacter.html", {"character": character})

def create(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        main_genre = request.POST.get('main_genre')
        description = request.POST.get('description')
        img_url = request.POST.get('img_url') or "no_image"
        status = request.POST.get('status')
        type_ = request.POST.get('type')

        Anime.objects.create(
            name=name,
            date=date,
            main_genre=main_genre,
            description=description,
            img_url=img_url,
            status=status,
            type=type_
        )

        return redirect('anime:index')

    return render(request, "animepage/createAnime.html")

def createCharacter(request, anime_id):

    anime = get_object_or_404(Anime, id=anime_id)

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST.get('age', 0)
        description = request.POST['description']
        img_url = request.POST.get('img_url', 'no_image')

        Character.objects.create(
            name=name,
            age=age,
            description=description,
            img_url=img_url,
            anime=anime
        )
        return redirect('anime:info', anime_id=anime.id)

    return render(request, "animepage/createCharacter.html", {"anime": anime})

def deleteAnime(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    if request.method == 'POST':
        anime.delete()
        return redirect('anime:index')  # redirige a la lista de animes
    return render(request, 'animepage/deleteAnime.html', {'anime': anime})

def deleteCharacter(request, anime_id, character_id):
    character = get_object_or_404(Character, id=character_id)
    anime_id = character.anime.id  # para redirigir después
    if request.method == 'POST':
        character.delete()
        return redirect('anime:info', anime_id=anime_id)
    return render(request, 'animepage/deleteCharacter.html', {'character': character})