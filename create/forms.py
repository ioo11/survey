from django import forms
from django.db import models

class NewTestForm(forms.Form):
    test_name = models.CharField(max_length=30)
    question_text  = models.CharField(max_length=250)
    answer_text = ''
    question_list = []