from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View

from .forms import ContactForm
from .models import ContactModel


class Contact(View):
    def get(self, request):
        contact = ContactForm()
        return render(request, 'contact/contact.html', {'contact': contact})

    def post(self, request):
        contact = ContactForm(request.POST)
        print(request.POST)
        if contact.is_valid():
            sql = ContactModel(
                name=contact.cleaned_data.get('name'),
                email=contact.cleaned_data.get('email'),
                subject=contact.cleaned_data.get('subject'),
                message=contact.cleaned_data.get('message'),

            )
            send_mail(contact.cleaned_data.get('subject'),
                      'name:' + contact.cleaned_data.get('name')
                      + '\nEmail:' + contact.cleaned_data.get('email')
                      + '\n\nMessages:\n' + contact.cleaned_data.get('message'),
                      'lotus.developer22@gmail.com', ['lotus.developer22@gmail.com'], fail_silently=False)

            sql.save()
        return render(request, 'contact/contact.html', {'contact': contact})
