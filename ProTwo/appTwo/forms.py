from django import forms
from django.core import validators


def check_for_p(value):
    if value[0].lower() != 'p':
        raise forms.ValidationError('Name must start with "P"')
    
class UserForm(forms.Form):
    name = forms.CharField(validators=[check_for_p])
    email = forms.EmailField(label='Your Email')
    confirm_email = forms.EmailField(label='Confirm your Email')
    address = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    # this is not needed                                                   
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('Got a bot')
        return botcatcher
    
    def clean(self) -> dict[str]:
        clean_all_data = super().clean()
        email = clean_all_data['email']
        confirm_email = clean_all_data['confirm_email']
        if email != confirm_email:
            raise forms.ValidationError('Your email did not match, Try again!')
