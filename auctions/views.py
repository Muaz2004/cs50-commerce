from django.shortcuts import render
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse


# Create your views here.

def index(request):
    query=active_lising.objects.all()
    return render(request,"auctions/index.html",{
        "query":query
        })
 
 

#def add(request):
    #if not request.user.is_authenticated:
        #return render(request,"users/login.html",{
           # "message":"you are not Eligable"
        #})
    #elif request.user.is_authenticated and request.method=="POST":
       # Title=request.POST.get("title")
       # Description=request.POST.get("description")
        #Starting_bid=request.POST.get("starting_bid")
        #Image_url=request.POST.get("image_url")
        #if Starting_bid.isdigit():
            #active_lising.objects.create(title=Title,description=Description,starting_bid=Starting_bid,image_url=Image_url)
            #return HttpResponseRedirect(reverse('index'))
        #else:
            #return render(request,"auctions/add.html",{
                #"message":"invalid input"
           # })
    #return render(request,"auctions/add.html")


def display(request,list_id):
    return render(request,"auctions/listings.html",{
        "query":active_lising.objects.get(pk=list_id)
    })

def add(request, list_id):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
            "message": "You need to be logged in to add to your watchlist"
        })
    
    listing = active_lising.objects.get(pk=list_id)
    # Get or create the watchlist for the user
    watchlist, created = Watchlist.objects.get_or_create(user=request.user)
    watchlist.watchlist.add(listing)
    return HttpResponseRedirect(reverse('index'))


def remove(request, list_id):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {
            "message": "You need to be logged in to remove from your watchlist"
        })
    else:
        try:
            # Get the listing by its ID
            listing = active_lising.objects.get(pk=list_id)
        except active_lising.DoesNotExist:
            return HttpResponse("Listing does not exist")
        
        # Get the user's watchlist
        user_watchlist = Watchlist.objects.filter(user=request.user).first()

        # Check if the listing is in the user's watchlist
        if user_watchlist and listing in user_watchlist.watchlist.all():
            user_watchlist.watchlist.remove(listing)
            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponse("Listing not found in your watchlist")
   














#def edit(request,list_id):
    #if not request.user.is_authenticated:
        #return render(request,"users/login.html",{
            #"message":"you are not Eligable"
       # })
    #elif request.user.is_authenticated and request.method=="POST":
        #Title=request.POST.get("title")
        #Description=request.POST.get("description")
        #Starting_bid=request.POST.get("starting_bid")
        #Image_url=request.POST.get("image_url")
        #edited=active_lising.objects.get(pk=list_id)
       # edited.title=Title
       # edited.description=Description
       # edited.starting_bid=Starting_bid
        #edited.image_url=Image_url
        #edited.save()
        #return HttpResponseRedirect(reverse('display',args=[list_id]))


    #return render(request,"auctions/edit.html",{
      #  "query":active_lising.objects.get(pk=list_id)
   # })

