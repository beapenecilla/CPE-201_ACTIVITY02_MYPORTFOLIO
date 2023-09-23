from django.shortcuts import render, HttpResponse

def home(request):
    # return HttpResponse("This is my home page (/)")
    # context =  { }
    context =
    return render(request, 'home.html')

def about(request):
  #  return HttpResponse("This is my about page (/about)")
  return render(request, 'about.html')

def project(request):
   # return HttpResponse("This is my project page (/project)")
    return render(request, 'about.project')

def contact(request):
   # return HttpResponse("This is my contact (/contact)")
   return render(request, 'about.contact')