from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  # model django post 
        if form.is_valid():
            form.save()
            return redirect("data_crypto:list")
    form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form":form})

def login_view(request):
    if request.method == "POST":
        print("CHECK1")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("CHECK2")
            user = form.get_user()
            login(request, user)
            return redirect("data_crypto:list")
    else:
        form = AuthenticationForm
    return render(request, "accounts/login.html", {"form":form})








# from django.shortcuts import render, HttpResponse
# from django.contrib.auth.forms import UserCreationForm

# def signup_view(request):
#     if request.method == "POST":
#        print("CHECK:", request.POST)
#        return HttpResponse(str(request.POST))
#     form = UserCreationForm()
#     return render(request, "accounts/signup.html", {"form":form})
