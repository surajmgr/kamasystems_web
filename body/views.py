from django.shortcuts import render, get_object_or_404
from .models import blog, project

# Create your views here.
def blogs(request):
    ablogs = blog.objects
    return render(request, 'body/blogs.html', {'ablogs':ablogs})

def projects(request):
    projs = project.objects
    return render(request, 'body/projects.html', {'projs':projs})

def projdetails(request, project_id):
    projdetail = get_object_or_404(project, pk=project_id)
    return render(request, 'body/projdetail.html', {'projdetail':projdetail})

def details(request, blog_id):
    blogdetail = get_object_or_404(blog, pk=blog_id)
    return render(request, 'body/detail.html', {'blogdetail':blogdetail})