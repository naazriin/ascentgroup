from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message sent succesfully!')
            return redirect('home_page')
        else:
            messages.add_message(request, messages.ERROR, 'Your message was not sent!')

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context=context)