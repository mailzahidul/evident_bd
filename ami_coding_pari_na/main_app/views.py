from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_admin.models import User
from django.contrib import messages
from user_admin.models import User as UUser
# Create your views here.

@login_required
def home(request):
    context={}
    return render(request, 'index.html', context)


@login_required
def quiz_list(request):
    context={}
    return render(request, 'main_app/quiz_list.html', context)

@login_required
def quiz_test(request, id):
   context={}


   return render(request, 'main_app/quiz_test.html', context)




def add_quiz(request):
    context={}
    return render(request, 'main_app/add_quiz.html', context)


def resutl_view(request):
    context={}
    return render(request, 'main_app/result.html', context)
