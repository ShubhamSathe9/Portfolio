from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from portfolio.models import *
from django.contrib import messages
# Create your views here.

def home(request):
    
    latest_projects = Project.objects.order_by('-id')[:3]   # ONLY 3


    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        datetime.today()
        
        contact = Contact(
        name=name, 
        email=email, 
        message = message, 
        date = datetime.today()
        )
        contact.save()
        
        messages.success(request, "Your mail is sent !!")
    
    
    return render(request, 'home.html', {"latest_projects": latest_projects})
    
def about(request):
    return render(request, 'about.html')
    
def projects(request):
    all_projects = Project.objects.all()
    return render(request, "projects.html", {"projects": all_projects})
   

def skills(request):
    skills = Skill.objects.all()
    return render(request, "skills.html", {"skills": skills})
    
def blog(request):
    return render(request, 'blog.html')
    
def services(request):
    return render(request, 'skills.html')
    
def contact(request):
    return render(request, 'contact.html')
    
    

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)

    # Get previous project
    previous_project = Project.objects.filter(id__lt=id).order_by('-id').first()

    # Get next project
    next_project = Project.objects.filter(id__gt=id).order_by('id').first()

    return render(request, "project_detail.html", {
        "project": project,
        "previous_project": previous_project,
        "next_project": next_project,
    })    
    
