from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.
# create a view that will be return by the view
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project': projectObj, 'tags': tags})

def createProject(request):
    projectform = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': projectform}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    projectform = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': projectform}
    return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    
    # logic to handle the post request to delete the record from the database.
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)