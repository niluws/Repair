from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.core.mail import send_mail
from authentication.models import User, Profile
from customer.models import CustomerItem,CustomerItemImage
from .forms import UserForm, ProfileForm,RequestForm,ChildModelFormSet


class CustomerStuffListView(ListView):
    template_name = 'customer/stuff.html'
    model = CustomerItem
    context_object_name = 'customerItems'
    paginate_by = 10


class CustomerStuffDetail(DetailView):
    template_name = 'customer/stuff_detail.html'
    model = CustomerItem
    context_object_name = 'customerDetailItems'


class CustomerRequest(View):
    def get(self, request):

        request_form = RequestForm()
        image_formset = ChildModelFormSet()
        print(image_formset)
        return render(request, 'customer/customer_request.html', {'request_form': request_form,'image_formset':image_formset})

    def post(self, request):
        request_form = RequestForm(request.POST)
        image_formset = ChildModelFormSet(request.POST, request.FILES)
        print(image_formset)
        if request_form.is_valid():
            sql = CustomerItem(
                user_id=request.user.id,
                title=request_form.cleaned_data.get('title'),
                description=request_form.cleaned_data.get('description'),
                status=True,


            )
        if request_form.is_valid() and image_formset.is_valid():
            customer_item = CustomerItem(
                user_id=request.user.id,
                title=request_form.cleaned_data.get('title'),
                description=request_form.cleaned_data.get('description'),
                status=True,

            )
            # send_mail(request_form.cleaned_data.get(customer_item.title),
            #           'name:' + request_form.cleaned_data.get(request.user.username)
            #           + '\nEmail:' + request_form.cleaned_data.get(request.user.email)
            #           + '\n\nMessages:\n' + request_form.cleaned_data.get(customer_item.description),
            #           'lotus.developer22@gmail.com', ['lotus.developer22@gmail.com'], fail_silently=False)

            customer_item.save()
            image_formset.instance = customer_item
            image_formset.save()


        return render(request, 'customer/customer_request.html', {'request_form': request_form,'image_formset':image_formset})


class CustomerProfileView(View):
    def get(self, request):
        current = User.objects.filter(id=request.user.id).first()
        currentProfile = Profile.objects.filter(user_id=request.user.id).first()
        userForm = UserForm(instance=current)
        profileForm = ProfileForm(instance=currentProfile)

        return render(request, 'customer/profile.html', {'userForm': userForm, 'profileForm': profileForm})


def update(request):
    current_user = request.user
    current_profile = Profile.objects.filter(user=current_user).first()
    user_form = UserForm(request.GET, instance=current_user)
    profile_form = ProfileForm(request.GET, instance=current_profile)

    if user_form.is_valid():
        user_form.save(commit=True)

    if profile_form.is_valid():
        profile = profile_form.save(commit=False)
        profile.user = current_user
        profile.save()

    return render(request, 'customer/profile_partial.html', {'userForm': user_form, 'profileForm': profile_form})
