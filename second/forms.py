from django import forms

from second.models import Profile

class ThisISForm(forms.ModelForm):

    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'address', 'city']
