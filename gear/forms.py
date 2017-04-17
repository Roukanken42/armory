from django import forms
from .models import Server

def get_servers():
    return [(None, "server")] + [
        (server.name, server.name)
        for server in Server.objects.all().order_by("region", "name")
    ] 

class PlayerSearchForm(forms.Form):
    player = forms.CharField(
        label = "Player", max_length = 30, required = False,
        # widget = forms.TextInput(attrs = {"placeholder": "Search player"})
    )
    server = forms.ChoiceField(choices = get_servers, required = False)
