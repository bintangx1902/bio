from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = MyProfile
        fields = ('nick', 'prof_img', 'f_name', 'w_phone', 'email', 'desc', )
