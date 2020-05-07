from django import forms
from .models import *


class AskForm(forms.Form):
    question = forms.Textarea()

