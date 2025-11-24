from django.shortcuts import  get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Anime, Character, Vote, Status, Genre
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from .forms import StatusForm, GenreForm, CreateAnime

def index(request):
    anime_list = Anime.objects.all()
    context = {"anime_list": anime_list}
    return render(request, "animepage/index.html", context)

class Info(DetailView):
    model = Anime
    template_name = "animepage/info.html"
    context_object_name = "info"

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

class CreateAnime(CreateView):
    model = Anime
    form_class = CreateAnime
    template_name = "animepage/createAnime.html"
    success_url = reverse_lazy('anime:index')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre.objects.all()
        context["status"] = Status.objects.all()
        return context

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
        return redirect('anime:index')  
    return render(request, 'animepage/deleteAnime.html', {'anime': anime})

def deleteCharacter(request, anime_id, character_id):
    character = get_object_or_404(Character, id=character_id)
    anime_id = character.anime.id  
    if request.method == 'POST':
        character.delete()
        return redirect('anime:info', anime_id=anime_id)
    return render(request, 'animepage/deleteCharacter.html', {'character': character})

def vote(request):
    if request.method == "POST":
        name = request.POST.get('name')
        score = request.POST.get('score')
        observation = request.POST.get('observation')

        Vote.objects.create(
                name=name,
                score=int(score),
                observation=observation
            )

        return redirect('anime:votes')
    
    return render(request, 'animepage/vote.html')

def votes(request):
    votes = Vote.objects.all()
    return render(request, 'animepage/votes.html', {'votes': votes})

def deleteVote(request, id):
    if request.method == "POST":    
        vote = get_object_or_404(Vote, id=id)
        vote.delete()
    return redirect('anime:votes')

def config(request):

    status_all = Status.objects.all()
    genre_all = Genre.objects.all()

    return render(request, 'animepage/config.html', {"status": status_all, "genres": genre_all})

class CreateStatus(CreateView):
    model = Status
    form_class = StatusForm
    template_name = "animepage/formStatus.html"
    success_url = reverse_lazy('anime:config')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accion"] = "Crear"
        return context

class DeleteStatus(DeleteView):
    model = Status
    template_name = "animepage/deleteStatus.html"
    context_object_name = "status"
    success_url = reverse_lazy('anime:config')

class EditStatus(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = "animepage/formStatus.html"
    success_url = reverse_lazy('anime:config')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accion"] = "Editar"
        return context
    
class CreateGenre(CreateView):
    model = Genre
    template_name = "animepage/formGenre.html"
    success_url = reverse_lazy("anime:config")
    form_class = GenreForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accion"] = "Crear"
        return context 
    
class EditGenre(UpdateView):
    model = Genre
    template_name = "animepage/formGenre.html"
    success_url = reverse_lazy("anime:config")
    form_class = GenreForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accion"] = "Actualizar"
        return context 
    
class DeleteGenre(DeleteView):
    model = Genre
    template_name = "animepage/deleteGenre.html"
    success_url = reverse_lazy("anime:config")
    context_object_name = "genre"