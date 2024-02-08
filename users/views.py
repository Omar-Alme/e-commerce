from django.contrib import messages
from allauth.account.views import SignupView
from users.forms import ExtendedSignupForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

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
    