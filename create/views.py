from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from .models import Test, RadioAnswer, Question, SetAnswer
from django.utils.encoding import smart_text
from django.utils import timezone


def index(request):
    return render(request, 'create/create.html')


def add_to_database(test_name, question_list, answer_list, question_types):
    # Saving test
    t = Test(name=str(test_name), pub_date=timezone.now())
    t.save()

    # saving questions
    q = []
    for i, j in question_list.items():
        question_type = question_types.get(i)
        q.append(Question(id_test=t, type=question_type, text=j))

    for i in q:
         i.save()

    # saving answers
    a = []
    for i, j in answer_list.items():
        if q[i].type == 'r':
            for k in j:
                a.append(RadioAnswer(id_question=q[i], text=k))
        elif q[i].type == 'e':
            for k in j:
                a.append(SetAnswer(id_question=q[i], text=k))
        elif q[i].type == 'text':
            pass

    for i in a:
        i.save()

def result(request):
    test_name = ''
    question_list = {}
    answer_list = {}
    response = ''
    question_types = {}

    for name, value in request.POST.items():
        # i -  j -
        if name[0:8] == 'question':
            question_id = int(name[14])  # question_text.0 <- 0 on 14 place
            question_text = value.encode('utf-8')
            question_list.update({question_id : question_text})

        elif name[0:11] == 'answer_text':
            question_id = int(name[12])  # answer_text.0 <- 0 on 12 place
            if not answer_list.get(question_id):
                answer_list.update({question_id : []})
            answer_list[question_id].append(value.encode('utf-8'))

        elif name[0:4] == 'test':
            test_name = value.encode('utf-8')

        elif name[0:11] == 'answer_type':
            question_id = int(name[12])  # answer_type.0 <- 0 on 12 place
            question_type = value.encode('utf-8')
            print ('in result: question_type = ' + question_type + 'question_id = ' + str(question_id))
            question_types.update({question_id : question_type})



    response += test_name + '\n<br>'

    for i, j in answer_list.items():
        temp = '; '.join([h for h in j])
        response += ': '.join((str(question_list.get(i)), temp)).strip()\
                    + "; type: "\
                    + str(question_types.get(i))\
                    + '\n<br>'


    add_to_database(test_name, question_list, answer_list, question_types)
    print(response)
    return HttpResponse(response)
