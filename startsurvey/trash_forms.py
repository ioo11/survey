from django import forms
from .models import Test, Question, SelectedRadioAnswer


class TestForm(forms.Form):
    def __init__(self, name='', questions=[], *args, **kwargs):
        super(TestForm, self).__init__()
        QuestionFormset = forms.formset_factory(forms.CheckboxSelectMultiple, extra=0)
        formset = QuestionFormset(initial={'choise':questions})
        # for i, question in enumerate(questions):
        #     self.fields['question_%s' % i] = QuestionForm()


class QuestionForm(forms.Form):
    def __init__(self, text='', answers=[], *args, **kwargs):
        super(QuestionForm, self).__init__()
        # text = forms.CharField(max_length=250)
        self.fields['text'] = text
        for i, answer in enumerate(answers):
            self.fields['answer_%s' % i] = AnswerForm()


class AnswerForm(forms.Form):
    def __init__(self, text='', *args, **kwargs):
        super(AnswerForm, self).__init__()
        # text = forms.CharField(max_length=250)
        self.fields['text']= text



class FieldsetWidget(forms.Widget):
    def render(self, name, value, attrs=None):
        return self.attrs['form_html']


class FieldsetField(forms.Field):
    def __init__(self, fieldset, *args, **kwargs):
        widget = FieldsetWidget(attrs={
            'form_html':'<div>%s</div>' % fieldset
        })
        kwargs.update({
            'widget': widget,
            'required': False
        })
        super(FieldsetField, self).__init__(*args, **kwargs)


# class TestForm(forms.Form):
#     def __init__(self, name='', questions=[], *args, **kwargs):
#         super(TestForm, self).__init__()
#
#         # InlineFormSet = forms.formset_factory(QuestionForm, extra=0)
#         # formset = InlineFormSet(prefix='formset', initial=questions)
#         #    self.fields['questions'] = FieldsetField(fieldset=formset, label=name)
#         self.fields['text'] = forms.BooleanField(label=name)
#         for i, question in enumerate(questions):
#             # self.fields['question_%s' % i] = FieldsetField(fieldset=formset, label='test_form')
#             self.fields['question_%s' % i] = FieldsetField(fieldset=question, label=question.get_label())
#
#
#
# class QuestionForm(forms.Form):
#     def __init__(self, text='question', answers=[], *args, **kwargs):
#         super(QuestionForm, self).__init__()
#         self.text = text
#         self.fields['answers'] = FieldsetField(fieldset=forms.CheckboxSelectMultiple(choices=answers))
#         # self.fields['text'] = forms.CharField(max_length=30)
#         # InlineFormSet = forms.formset_factory(AnswerForm)
#         # formset = InlineFormSet(prefix='formset', initial=answers)
#         # self.fields['answer'] = FieldsetField(fieldset=formset, label=text)
#         # for i, answer in enumerate(answers):
#             # # self.fields['answer_%s' % i] = FieldsetField(fieldset=formset, label='question_form')
#             # self.fields['answer_%s' % i] = forms.BooleanField(label=answer.get_label())
#             # # self.fields['answer_%s' % i] = FieldsetField(fieldset=answer, label=answer.get_label())
#
#     def get_label(self):
#         return self.text
#
#
# class AnswerForm(forms.Form):
#     def __init__(self, text='answer', *args, **kwargs):
#         super(AnswerForm, self).__init__()
#         self.text = forms.BooleanField(label=text, required=False)
#         # self.fields['text']= text
#     def get_label(self):
#         return self.text.label



