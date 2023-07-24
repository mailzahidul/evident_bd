from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_admin.models import User
from datetime import datetime
from .models import InputValue
from django.contrib import messages
# Create your views here.

@login_required
def home(request):
    context={}
    datetime_format = '%d-%m-%Y %H:%M:%S'
    login_user = request.user
    user_id = User.objects.get(email=login_user)
    if request.method == 'POST':
        timestamp = datetime.now().strftime(datetime_format)
        input_values = request.POST['input_values']
        InputValue.objects.create(user=user_id, timestamp=timestamp, input_values=input_values)

    return render(request, 'index.html', context)