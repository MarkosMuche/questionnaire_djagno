from django.urls import path
from . import views

urlpatterns = [
    path('person_question/', views.person_question, name='person_question'),
    path('companyform/', views.company_question, name='ask_question'),

]