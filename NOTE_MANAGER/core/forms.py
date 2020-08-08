from django import forms

class NoteForm(forms.Form):
    title=forms.CharField(label="Title",max_length=255,widget=forms.TextInput(attrs={}))
    description=forms.CharField(label="Description",widget=forms.Textarea())

