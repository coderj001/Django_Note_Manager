from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
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
        form=NoteForm(request.POST)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            title=form.cleaned_data["title"]
            description=form.cleaned_data["description"]
            note=Note.objects.create(title=title,description=description)
            note.save()
            messages.success(request,'Note Is Added!')
            return redirect("core:note",id=note.id)
        else:
            messages.info(request,str(form.errors))
            return redirect("core:addnote")


def notelist(request,id):
    if request.method=="GET":
        note=get_object_or_404(Note, id=id)
        notes_list=Note.objects.all()
        return render(request,"home.html",context={
            "notes_list":notes_list,
            "note":note,
        })
    if request.method=="POST":
        form=NoteForm(request.POST)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            note=get_object_or_404(Note,id=id)
            note.title=form.cleaned_data["title"]
            note.description=form.cleaned_data["description"]
            note.save()
            messages.success(request,'Note Is Updated!')
            return redirect("core:note",id=note.id)
        else:
            messages.info(request,str(form.errors))
            return redirect("core:addnote")
        
def notedelete(request,id):
    if request.method=="GET":
        note=get_object_or_404(Note, id=id)
        note.delete()
        messages.warning(request,'Note Is Deleted!')
        return redirect("core:addnote")

