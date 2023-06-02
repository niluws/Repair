from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class': 'form-control border-0 bg-light px-4', 'placeholder': "First name", 'style': "height: 55px;"}))
    last_name = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class': 'form-control border-0 bg-light px-4', 'placeholder': "Last name", 'style': "height: 55px;"}))
    username = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class': 'form-control border-0 bg-light px-4', 'placeholder': " Username", 'style': "height: 55px;"}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget=forms.EmailInput(attrs={'class': 'form-control border-0 bg-light px-4', 'placeholder': "Email", 'style': "height: 55px;"}))
    password = forms.CharField(max_length=254,widget=forms.PasswordInput(attrs={'class': 'form-control border-0 bg-light px-4', 'placeholder': "password", 'style': "height: 55px;"}))
    password2 = forms.CharField(max_length=254,widget=forms.PasswordInput(attrs={'class': 'form-control border-0 bg-light px-4', 'placeholder': "Confirm password", 'style': "height: 55px;"}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password'),
        password2 = self.cleaned_data.get('password2'),
        if password == password2:
            return password2


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control border-0 bg-light px-4', 'placeholder': "Username", 'style': "height: 55px;"}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(
        attrs={'class': 'form-control border-0 bg-light px-4', 'placeholder': "Password", 'style': "height: 55px;"}))
