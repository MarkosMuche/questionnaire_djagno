from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('get_vision/', submit_values, name='get-vision'),
    path('', person_question, name='person_question'),
    path('company_question', company_question, name='ask_question'),
    path('display-values/', display_company_values, name='display_values'),

]