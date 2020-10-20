from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm
# Create your views here.
from .utilities import fetch_data
from .models import Post

def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            txt = form.cleaned_data.get('product')
            price1 = form.cleaned_data.get('min_price')
            price2 = form.cleaned_data.get('max_price')
            checkbox = form.cleaned_data.get('checkbox')
            sumoftheProducts = fetch_data(txt,price1,price2)
            ls = sumoftheProducts[0]
            eshops = sumoftheProducts[1]
            context = {'context': ls,'eshops': eshops,'form': form}
            return render(request, "app/home.html", context=context)


    form = SearchForm()
    context = {'context':'', 'form': form}
    return render(request, "app/index.html", context=context)

