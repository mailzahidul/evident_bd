from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_admin.models import User
from datetime import datetime
from .models import InputValue
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import InputValueSerializer
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


class ShowInputValueView(APIView):
    # Get all objects
    def get_object(self, id):
        try:
            input_values = InputValue.objects.filter(user=id)
            return input_values
        except:
            raise Http404
    def get(self, request, id):
        input_values = self.get_object(id=id)
        if not input_values:
            return Response({"status": False, "message": 'No Object', "code": 400})
        serializer = InputValueSerializer(input_values, many=True)
        return Response({"status": 'success',"user_id": id, "payload": serializer.data})

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)