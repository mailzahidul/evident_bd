from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_admin.models import User
from datetime import datetime
from .models import InputValue
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import InputValueSerializer
import requests
from django.http import Http404
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


def input_values(request):
    context = {}
    login_user = request.user
    user_id = User.objects.get(email=login_user)
    url = 'http://127.0.0.1:8000/list_input_values'
    if request.method == 'POST':
        token = '3323da613dc98ece7d0f2d25011b48fd022304d3'
        from_datetime = request.POST['from_datetime']
        to_datetime = request.POST['to_datetime']
        print(request.POST,'ppppppppppppppp')
        header = {"Authorization": f'Token {token}'}
        try:
            response = requests.get(url, headers=header, data={"user_id":user_id.id, "from_datetime":from_datetime, "to_datetime":to_datetime}).json()
            print(response, '------------------')
        except Exception as err:
            print(err,'==00000000000000000')

        # context['input_values'] = response
    return render(request, 'index.html', context)


class ShowInputValueView(APIView):
    permissions_classes = [IsAuthenticated]
    def get(self, request):
        user = request.data['user_id']
        from_datetime = request.data['from_datetime']
        to_datetime = request.data['to_datetime']
        print(request.data,'=====================')
        input_values = InputValue.objects.filter(user=user, timestamp__gte=from_datetime, timestamp__lte=to_datetime)

        if not input_values:
            return Response({"status": False, "message": 'No Object', "code": 400})
        serializer = InputValueSerializer(input_values, many=True)
        return Response({"status": 'success',"user_id": id, "payload": serializer.data})
