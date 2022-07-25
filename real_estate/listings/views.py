from django.shortcuts import render, redirect
from .models import *
from .forms import ListingForm
#from .filter import Search
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
# CRUD - create, retrieve, update, delete, list

def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)


def listing_retrieve(request, pk):
    listing = Listing.objects.get(id = pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)


def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect("/")

    context = {
        "form" : form
    }
    return render(request, "listing_create.html", context)


def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)

def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")



def searchBar(request):
    if request.method == 'POST':
        #searched = 'searched' in request.POST and request.POST['searched']
        searched = request.POST['searched']
        results = Listing.objects.filter(title__contains=searched)
 
        return render(request, "search.html", {'searched': searched, 'results': results})
    else:
        return render(request, "search.html")
