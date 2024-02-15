from django import forms

from apps.models import Workers


class UserForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = '__all__'
