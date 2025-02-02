from django import forms
from django.contrib.auth.models import User
from .models import Technician

class TechnicianRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Technician
        fields = ['first_name', 'last_name', 'email', 'bio', 'shop']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
