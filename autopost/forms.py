from django import forms
from . import models


class AutopostForm(forms.ModelForm):
    class Meta:
        model = models.Autopost
        fields = ('id','title','siteurl', 'posturl','selection','gettag')

class AutopostCreateForm(forms.ModelForm):
    class Meta:
        model = models.Autopost
        fields = ('title', 'siteurl', 'posturl','selection','gettag')