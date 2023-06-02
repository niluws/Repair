from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, reverse
from django.utils.crypto import get_random_string
from django.views import View
from authentication.models import User
from .forms import SignUpForm, LoginForm
from utils.email_service import send_email

class SignupView(View):


    def get(self, request):
        form = SignUpForm(request.GET)
        return render(request, 'authentication/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            email_exist: bool = User.objects.filter(email__iexact=email).exists()
            user: bool = User.objects.filter(username__iexact=username).exists()

            if email_exist:
                form.add_error('email', 'email is exist')
            else:
                if user:
                    form.add_error('username', 'username is exist')
                    redirect(reverse('register'))
                else:

                        new_user = User(
                            first_name=first_name,
                            last_name=last_name,
                            username=username,
                            email=email,
                            active_code=get_random_string(47),
                            is_active=False,
                            is_staff=False,

                        )
                        new_user.set_password(password)
                        new_user.save()
                        send_email('activation', new_user.email, {'user': new_user}, 'emails/activate_account.html')

        return render(request, 'authentication/signup.html', {'form': form})


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'authentication/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username__iexact=username).first()
            if user is not None:

                if not user.is_active:
                    form.add_error('username', 'username is not activate')

                else:
                    is_password_correct = user.check_password(password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home'))
                    else:
                        form.add_error('password', 'password is wrong')

            else:
                form.add_error('username', 'username is not exist')

        return render(request, 'authentication/login.html', {'form': form})

class Activation(View):
    def get(self, request, active_code):
        user: User = User.objects.filter(active_code__iexact=active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.active_code = get_random_string(47)
                user.save()
                return redirect(reverse('login'))
            else:
                print('its activated')
        else:
            print('code is broken')

        return redirect(reverse('login'))
def Logout(request):
    logout(request)
    return redirect(reverse('home'))
