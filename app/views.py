# myapp/views.py

from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CompanyValueForm,PersonValueForm,AnswerForm
from ai_utils.utils import get_vision_statement,get_company_value,get_person_value,get_value_ideas
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


def company_question(request):
    if request.method == "POST":
        form = CompanyValueForm(request.POST)
        if form.is_valid():
            questions_and_answers = ""
            for field_name, field_value in form.cleaned_data.items():
                questions_and_answers += f"Q: {field_name}\nA: {field_value}\n\n"
            company_value = get_company_value(questions_and_answers)
            return render(request, 'company_value_list.html', {'company_value': company_value})
    else:
        form = CompanyValueForm()

    return render(request, 'company_value_from.html', {'form': form})



def person_question(request):
    questions = Question.objects.all()
    num_questions = questions.count()
    current_question_index = request.session.get('current_question_index', 0)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            request.session[f'answers_for_question_{current_question_index + 1}'] = [
                form.cleaned_data['answer_1'],
                form.cleaned_data['answer_2'],
                form.cleaned_data['answer_3'],
                form.cleaned_data['answer_4']
            ]

            if current_question_index == num_questions - 1:
                questions_and_answers = ''
                for i in range(num_questions):
                    question_text = questions[i].text
                    answers = request.session.get(f'answers_for_question_{i + 1}', [])
                    questions_and_answers += f"Q: {question_text}\nA: {', '.join(answers)}\n\n"
                person_value = get_person_value(questions_and_answers)
                request.session['person_value'] = person_value  # Store in session
                # request.session.flush()
                return redirect('ask_question')


            request.session['current_question_index'] = current_question_index + 1
            return redirect('person_question')

    else:
        current_question = questions[current_question_index]
        form = AnswerForm()

    context = {
        'form': form,
        'question_text': current_question.text,
        'is_last_question': current_question_index == num_questions - 1
    }

    return render(request, 'person_value_form.html', context)


def submit_values(request):
    if request.method == 'POST':
        company_values = request.POST.getlist('company_values')
        other_values = request.POST.getlist('other_value')
        company_values.extend(other_values)  # Combine the lists

        person_values = request.session.get('person_value', None)
        request.session.flush()
        User = get_user_model()
        user_instance = User.objects.get(pk=1) 
        for company_value in company_values:
            # Save or retrieve the company value
            company_value_obj, created = CompanyValue.objects.get_or_create(value=company_value,user=user_instance)
            ideas = get_value_ideas(company_value)
            print(ideas)
            x=0
            for  idea in ideas:
                x=x+1
                print(x)
                VisionIdea.objects.create(company_value=company_value_obj, idea=idea)

    return redirect('display_values')




def display_company_values(request):
    if request.user.is_authenticated:
        # Fetch the four latest company values for the logged-in user
        # Order by 'created_at' to get the most recent, or use '-id' for the latest by ID
        User = get_user_model()
        user_instance = User.objects.get(pk=1) 
        company_values = CompanyValue.objects.filter(user=user_instance).order_by('-created_at')[:4]

        data = [{
            'value': value,
            'ideas': value.vision_ideas.all()
        } for value in company_values]

        return render(request, 'company_values.html', {'data': data})
    