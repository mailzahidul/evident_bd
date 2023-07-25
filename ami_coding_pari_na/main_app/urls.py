from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('list_input_values', views.ShowInputValueView.as_view()),
    path('input_values', views.input_values, name="input-values" ),
]
