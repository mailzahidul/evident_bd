from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('list_input_values/<int:id>', views.ShowInputValueView.as_view()),
    path('hello/', views.HelloView.as_view(), name='hello'),
]
