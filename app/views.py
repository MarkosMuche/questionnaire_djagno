# myapp/views.py

from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CompanyValueForm,PersonValueForm,AnswerForm
from ai_utils.utils import get_vision_statement,get_company_value,get_person_value
from .models import *



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
            # Save answers to session
            request.session[f'answers_for_question_{current_question_index + 1}'] = [
                form.cleaned_data['answer_1'],
                form.cleaned_data['answer_2'],
                form.cleaned_data['answer_3'],
                form.cleaned_data['answer_4']
            ]

            # If it's the last question
            if current_question_index == num_questions - 1:
                questions_and_answers = ''
                for i in range(num_questions):
                    question_text = questions[i].text
                    answers = request.session.get(f'answers_for_question_{i + 1}', [])
                    questions_and_answers += f"Q: {question_text}\nA: {', '.join(answers)}\n\n"
                print(questions_and_answers)
                person_value = get_person_value(questions_and_answers)
                request.session.flush()
                return render(request, 'person_value_list.html', {'company_value': person_value})

            # Otherwise move to the next question
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
        selected_values = request.POST.getlist('company_values')
        other_value = request.POST.get('other_value', '').strip()

        if other_value:
            selected_values.append(other_value)
        print(selected_values)

        # Ensure that no more than 4 values are selected
        selected_values = selected_values[:4]

        # Process the values...
        return HttpResponse("Values processed")
    else:
        return HttpResponse("Invalid request")
