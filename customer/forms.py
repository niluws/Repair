from django import forms
from authentication.models import User,Profile
from .models import CustomerItem,CustomerItemImage
from django.forms import inlineformset_factory

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name', 'last_name','username' ,'email']
        widgets={
            'first_name' : forms.TextInput(attrs={'id':'first_name','class': 'form-control border-0 bg-light px-4', 'placeholder': "First name",'style': "height: 55px;"}),
        'last_name' : forms.TextInput(attrs={'id':'last_name','class': 'form-control border-0 bg-light px-4', 'placeholder': "Last name",'style': "height: 55px;"}),
        'username' : forms.TextInput(attrs={'id':'username','class': 'form-control border-0 bg-light px-4', 'placeholder': " Username",'style': "height: 55px;"}),
        'email' : forms.EmailInput(attrs={'id':'email','class': 'form-control border-0 bg-light px-4', 'placeholder': "Email", 'style': "height: 55px;"}),

        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['post_code', 'address', 'phone']
        widgets = {
            'post_code': forms.TextInput(attrs={'id':'post_code','class': 'form-control border-0 bg-light px-4', 'placeholder': "post code",'style': "height: 55px;"}),
            'address': forms.TextInput(attrs={'id':'address','class': 'form-control border-0 bg-light px-4', 'placeholder': "Fars , Shiraz ,Farhangian",'style': "height: 55px;"}),
            'phone': forms.TextInput(attrs={'id':'phone','class': 'form-control border-0 bg-light px-4', 'placeholder': "(+98) 912-222-7482",'style': "height: 55px;"}),
        }

class CustomerItemImageForm(forms.ModelForm):
    class Meta:
        model = CustomerItemImage
        fields = ['image_file']
        widgets = {
            'image_file': forms.FileInput(attrs={'id':'image','class': '','style': "height: 55px;"}),
        }

class RequestForm(forms.ModelForm):
    class Meta:
        model = CustomerItem
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'id':'title','class': 'form-control border-0 bg-light px-4', 'placeholder': "title",'style': "height: 55px;"}),
            'description': forms.Textarea(attrs={'id':'description','class': 'form-control border-0 bg-light px-4 py-3','row' :'4', 'placeholder': "description"}),
        }

ChildModelFormSet = inlineformset_factory(
    CustomerItem,  # Parent model
    CustomerItemImage,  # Child model
    form=CustomerItemImageForm,  # Use the form for the ChildModel
    extra=1,
can_delete=False
)