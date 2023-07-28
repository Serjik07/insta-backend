from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Login
# Create your views here.
def esim(requset):
    log = Login.objects.all()
    return render(requset, "main/esim.html",{"login": log})

def home(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            print("error")

    return render(request,"main/index.html", {"form":form})