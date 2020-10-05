from django import forms


class SearchForm(forms.Form):
    product = forms.CharField(widget=forms.TextInput(attrs={'id' : 'search','placeholder' : 'What are you looking for?'}))
    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'location','placeholder' : 'minimum '}))
    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'location','placeholder' : 'maximum '}))

