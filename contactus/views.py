from django.shortcuts import render
from .models import Contact, ContactInformation
from .forms import ContactUsForm


def contactUs(request):
    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']

            Contact.objects.create(name=name, email=email, title=title, body=body)
    else:
        form = ContactUsForm()

    contact = ContactInformation.objects.all().last()
    return render(request, 'contactus/contact.html', context={'form': form, 'contact': contact})