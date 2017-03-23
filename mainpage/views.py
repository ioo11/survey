from django.shortcuts import render #, render_to_response

# Create your views here.

from .models import Test
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    auth_form = AuthenticationForm()
    latest_tests = Test.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('mainpage/main.html')
    for i in latest_tests:
        print(i)
    context = {
        'form': auth_form,
        'latest_tests': latest_tests,
        }
    return render(request, 'mainpage/main.html', context)
    # return render_to_response('mainpage/inputform.html', locals())