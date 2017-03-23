from django import forms
from .models import Test, Question, SelectedRadioAnswer

class TestForm(forms.Form):
    def __init__(self, test):
        super(TestForm, self).__init__()

