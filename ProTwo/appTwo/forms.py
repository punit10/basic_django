from django import forms
from django.core import validators
from appTwo.models import Users


def check_for_p(value):
    if value[0].lower() != 'p':
        raise forms.ValidationError('Name must start with "P"')
    
class NewUserForm(forms.ModelForm):
    class Meta:
        model = Users
        # fields = ['name', 'email', 'confirm_email', 'address']
        fields = '__all__'
        
    # name = forms.CharField(validators=[check_for_p])
    # email = forms.EmailField(label='Your Email')
    # confirm_email = forms.EmailField(label='Confirm your Email')
    # address = forms.CharField(widget=forms.Textarea)


    # this is not needed                                                   
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('Got a bot')
        return botcatcher
        
# Form with database connect
        
