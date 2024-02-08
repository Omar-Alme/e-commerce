from allauth.account.forms import SignupForm
from django import forms


class ExtendedSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    def __init__(self, *args, **kwargs):
        super(ExtendedSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': True})    

    def save(self, request):
        user = super(ExtendedSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user