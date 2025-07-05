from django import forms
from home.models import registerAdmin

class REGISTERform(forms.ModelForm):

    class Meta:
        model = registerAdmin
        fields = ['name','email','password',]
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'})

} 
