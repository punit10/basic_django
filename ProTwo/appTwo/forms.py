from django import forms


class UserForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput)
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('Got a bot')
        return botcatcher
    