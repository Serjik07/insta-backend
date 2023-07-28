from django.shortcuts import render, redirect
from .forms import LoginForm
# Create your views here.

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