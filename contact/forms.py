from django import forms
class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput     (attrs={'style':"height: 55px",'class':"form-control border-0 bg-light px-4", 'id':"name" ,'placeholder':"Your Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'style':"height: 55px",'class':"form-control border-0 bg-light px-4", 'id':"email" ,'placeholder':"Your Email"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'style':"height: 55px",'class':"form-control border-0 bg-light px-4", 'id':"subject" ,'placeholder':"Subject"}))
    message = forms.CharField(widget=forms.Textarea (attrs={'class':"form-control border-0 bg-light px-4 py-3",'row' :'4','id':"message" ,'placeholder':"Message"}))