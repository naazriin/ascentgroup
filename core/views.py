from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm

from .models import Project, Partner, Video, Banner
from products.models import Product

def home(request):
    banner = Banner.objects.all()
    products = Product.objects.all()
    projects = Project.objects.all()
    partners = Partner.objects.all()
    videos = Video.objects.all()

    context = {
        'banner': banner,
        'products': products,
        'projects': projects,
        'partners': partners,
        'videos': videos,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message sent succesfully!')
            return redirect('contact_page')
        else:
            messages.add_message(request, messages.ERROR, 'Your message was not sent!')

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context=context)