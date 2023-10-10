from django import forms

class PokemonForm(forms.Form):
    pokemon_name = forms.CharField(label='pokemon Name', max_length=100)