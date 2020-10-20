from django import forms

sortup=[('item1','item 1')]
sortdown=[('item1','item 1')]
class SearchForm(forms.Form):
    product = forms.CharField(widget=forms.TextInput(attrs={'id' : 'search','placeholder' : 'Search a product'}))
    min_price = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class' : 'location','placeholder' : 'minimum '}))
    max_price = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class' : 'location','placeholder' : 'maximum '}))
    checkbox = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class':'checkbox','type':'checkbox'}))
