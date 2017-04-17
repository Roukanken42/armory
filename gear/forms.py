from django import forms
from .models import Server

def get_servers():
    return [(None, "------")] + [
        (server.name, server.name)
        for server in Server.objects.all()
    ] 

class PlayerSearchForm(forms.Form):
    player_name = forms.CharField(label = "Player name", max_length = 30, required = False)
    server = forms.ChoiceField(choices = get_servers, required = False)
