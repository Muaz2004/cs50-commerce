from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import login,authenticate,logout


# Create your views here.
def index(request):
    return render(request,"users/index.html")

def login_request(request):
    if request.method == "POST":
        Username = request.POST.get("username")
        Password = request.POST.get("password")
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            return HttpResponseRedirect(reverse("add"))
    return render(request, "users/login.html")

        


def logout_request(request):
    logout(request)
    return render(request,"users/login.html",{"message":"LOGGED_OUT"})
 