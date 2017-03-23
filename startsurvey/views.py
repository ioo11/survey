from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import TestForm
# Create your views here.

from .models import Test, Question, RadioAnswer, SetAnswer
from django.core.urlresolvers import reverse


def index(request):
    latest_tests = Test.objects.order_by('-pub_date')
    context = {
        'latest_tests': latest_tests,
    }
    return render(request, 'start/index.html', context)


def start(request, test_id):
    class MyTest:
        """
        Test:
            id
            name;
            Questionlist:
                question_1:
                    id;
                    text;
                    answer_list:
                        answer_1:
                            id
                            text

        """

        def __init__(self, name='', id=None, questoin_list=[]):
            self.name = name
            self.id = id
            self.question_list = questoin_list

        def add_question(self, question):
            self.question_list.append(question)

    class MyQuestion:
        def __init__(self, text='', id=None, answer_list=[], type = ''):
            self.text = text
            self.id = id
            self.type = type
            self.answer_list = answer_list  # answer: {id, text}

        def add_answer(self, answer):
            self.answer_list.append(answer)

    class MyAnswer:
        def __init__(self, text = '', id = None, question_id = None):
            self.text = text
            self.id = id
            self.question_id = question_id

    test = get_object_or_404(Test, pk=test_id)
    question_list = get_list_or_404(Question, id_test=test.id)
    test_class = MyTest(id=test.id, name=test.name.encode('utf-8'))
    debug = ''

    if request.method == 'POST':
        for i, j in request.POST.items():

            debug += i.encode('utf-8') + ': ' + j.encode('utf-8')
        return render(request, 'start/start.html', {'Test': test_class, 'debug': debug})
    else:
        for question in question_list:
            temp = MyQuestion(id = question.id, text=question.text.encode('utf-8'))

            debug += question.type
            if question.type == 'r' or question.type ==  'e':
                answers = []
                if question.type == 'r':
                    answers = get_list_or_404(RadioAnswer, id_question=question.id)
                    temp.type = 'radio'
                elif question.type == 'e':
                    answers = get_list_or_404(SetAnswer, id_question=question.id)
                    temp.type = 'checkbox'
                # answers = get_list_or_404(answer_type, id_question = question.id)

                debug += temp.text.decode('utf-8')
                for answer in answers:
                    temp_answer = MyAnswer(text=answer.text, id=answer.id, question_id=question.id)
                    temp.add_answer(temp_answer)
                    debug += answer.text
            else:
                debug += ' text'
                temp.type = 'text'
            test_class.add_question(temp)

        return render(request, 'start/start.html', {'Test': test_class, 'debug':debug})
