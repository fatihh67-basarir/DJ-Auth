from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'user_example/index.html')

def special(request):
    return render(request, "user_example/special.html")

def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect("home")

    context = {
        'form': form
    }
    return render(request, "registration/register.html", context)

    