from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm
# Create your views here.


def projects(request):
    projects = Project.objects.all()
    data = {
        'projects': projects
    }
    return render(request, 'projects.html', data)

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    data = {
        'form': form
    }

    return render(request, 'create_form.html', data)