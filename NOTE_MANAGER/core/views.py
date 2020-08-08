from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from core.models import Note
from core.forms import NoteForm

# Create your views here.

def demo(request):
    return HttpResponse("<h1>Hello World!</h1>")

def addnote(request):
    if request.method=="GET":
        notes_list=Note.objects.all()
        return render(request,"home.html",context={
            "notes_list":notes_list,
        })
    if request.method=="POST":
        # import pdb; pdb.set_trace()
        # BUG
        form=NoteForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            description=form.cleaned_data["description"]
            note=Note.objects.create(title=title,description=description)
            note.save()
            return redirect("core:note",id=note.id)

def notelist(request,id):
    if request.method=="GET":
        note=get_object_or_404(Note, id=id)
        notes_list=Note.objects.all()
        return render(request,"home.html",context={
            "notes_list":notes_list,
            "note":note,
        })
