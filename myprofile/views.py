from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,'base.html')
def projects(request):
    #return HttpResponse("<p>Profile page of user</p>")
    return render(request,'projects.html')
def resume(request):
    return render(request,'resume.html')
def about(request):
    return render(request,'about.html')
