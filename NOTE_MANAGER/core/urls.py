from django.urls import path
from core.views import (
    demo,
    addnote,
    notelist,
    notedelete
)

app_name='core'

urlpatterns = [
    # path('',demo,name="demo"),
    path('',addnote,name="addnote"),
    path('note/<id>',notelist,name="note"),
    path('notedelete/<id>',notedelete,name="delete"),
]
