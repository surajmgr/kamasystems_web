from django.shortcuts import render, HttpResponseRedirect
from .models import topProjects, featurette, contact
from .forms import ContactForm
from django.db.models import Q
# Create your views here.

def home(request):
    topProject = topProjects.objects
    featurettes = featurette.objects

    return render(request, 'jobs/home.html', {'tPrj':topProject,'ftr':featurettes})

def contacts(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/fdbk/msg')
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'jobs/contact.html', context)

def contactlst(request):
    lst = contact.objects
    return render(request, 'jobs/contactslist.html', {'clist':lst})

def privacy(request):
    return render(request, 'jobs/privacy.html')

def terms(request):
    return render(request, 'jobs/termscondition.html')

def error_404(request, exception=None):
    return render(request, 'jobs/error_404.html')

def error_500(request):
    data={}
    return render(request, 'jobs/error_500.html', data)