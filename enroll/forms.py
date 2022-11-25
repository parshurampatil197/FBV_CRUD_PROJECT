from django import forms
from .models import User

class StudentRegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True ,attrs={'class':'form-control'}),
        }

    # Check if a string contains a number
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     if (i.isdigit for i in valname):
    #         raise forms.ValidationError('Name should not contain a number')
    #     return valname