from django.shortcuts import render


# Create your views here.


def home(request):

    return render(request, 'devkid/home.html')



def about(request):
    return render(request, 'devkid/about.html')