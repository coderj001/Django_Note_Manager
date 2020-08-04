from django.urls import path,include
from core.views import (
    demo,
    home,
)

app_name='core'

urlpatterns = [
    #path('',demo,name="demo"),
    path('',home,name="home"),
]
