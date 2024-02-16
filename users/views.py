from django.contrib import messages
from allauth.account.views import SignupView
from users.forms import ExtendedSignupForm, UserForm, UserProfileForm
from users.models import UserProfile, User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import requests
from orders.models import Order


@login_required
def dashboard(request):
    """ A view to return the dashboard page """

    orders = Order.objects.order_by('-created_at').filter(
        user=request.user, is_ordered=True)
    order_count = orders.count()

    userprofile = UserProfile.objects.get(user=request.user)

    context = {
        'orders': orders,
        'order_count': order_count,
        'userprofile': userprofile,
    }

    return render(request, 'users/dashboard.html', context)


class ExtendedSignupView(SignupView):
    form_class = ExtendedSignupForm
    template_name = 'account/signup.html'

    def get_context_data(self, **kwargs):
        ret = super(ExtendedSignupView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret

    def form_valid(self, form):
        response = super(ExtendedSignupView, self).form_valid(form)
        messages.success(self.request, 'You have signed up successfully')
        return response


def order_history(request):
    """ A view to return the order history page """

    orders = Order.objects.filter(
        user=request.user, is_ordered=True).order_by('-created_at')

    context = {
        'orders': orders,
    }

    return render(request, 'users/order_history.html', context)


def edit_profile(request):
    """ A view to return the edit profile page """
    
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=userprofile
            )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated')

            return redirect('edit_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    }

    return render(request, 'users/edit_profile.html', context)
