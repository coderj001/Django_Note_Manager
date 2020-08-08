from django.urls import path
from core.views import (
    demo,
    addnote,
    notelist,
)

app_name='core'

urlpatterns = [
    # path('',demo,name="demo"),
    path('',addnote,name="addnote"),
	#TODO: Add function
    path('note/<id>',notelist,name="note"),
]
