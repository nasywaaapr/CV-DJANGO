from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'myApp/home.html')

def pendidikan(request):
    return render(request,'myApp/pendidikan.html')

def pengalaman(request):
    return render(request,'myApp/pengalaman.html')

def sosialmedia(request):
    return render(request,'myApp/sosialmedia.html')
