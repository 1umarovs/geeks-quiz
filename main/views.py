from django.shortcuts import render, redirect
from .models import Lead, Answer, Question


import re
import requests

def home(request):
    bot = "7567030915:AAGP4eremQ68lNU97zshb31NAirQ_0uTYeg"
    chat_id = "-1002458346219"
    name = request.POST.get('name', '').strip()
    age = request.POST.get('age', '').strip()
    phoneNumber = request.POST.get('phone', '').strip()
    error_message = None

    if request.method == 'POST' and any([name, age, phoneNumber]):
        if Lead.objects.filter(phoneNumber=phoneNumber).exists():
            error_message = "Bu telefon raqami allaqachon ro‘yxatdan o‘tgan."
        elif not re.match(r'^[A-Za-zА-Яа-я\s]+$', name):
            error_message = "Ism faqat harflardan iborat bo'lishi kerak."
        elif not age.isdigit() or not (10 <= int(age) <= 100):
            error_message = "Katta yoki kichik yosh kiritib yubordingiz."
        elif not re.match(r'^\+998 \(\d{2}\) \d{3} \d{2}-\d{2}$', phoneNumber):
            error_message = "Telefon raqami +998 (xx) xxx xx-xx formatida bo'lishi kerak."

        if error_message:
            context = {'error_message': error_message}
            return render(request, 'index.html', context)

        lead = Lead(name=name, age=age, phoneNumber=phoneNumber)
        lead.save()

        message = (
            f"🆕 Yangi Lead qo'shildi:\n"
            f"👤 Ismi: {name}\n"
            f"🎂 Yoshi: {age}\n"
            f"📞 Telefon raqami: {phoneNumber}"
        )
        send_telegram_message(bot, chat_id, message)

        return redirect('main:quiz')

    return render(request, 'index.html')

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML",
    }
    requests.post(url, data=payload)


def quiz(request):
    questions = Question.objects.all()
    questions_with_answers = []

    for q in questions:
        answers = Answer.objects.filter(question=q)
        questions_with_answers.append({
            'question': q,
            'answers': answers,
        })

    context = {
        'questions_with_answers': questions_with_answers,
    }

    return render(request, 'quiz.html', context)




# def result(request):
#     if request.method == "POST":
#         selected_answers = request.POST.getlist('answers') 
#         print(selected_answers)
#         count = {}
#         percentages = {}
#         categories = set() 

#         for answer_text in selected_answers:
#             answer_set = Answer.objects.filter(answer_text=answer_text).order_by('-id')
#             if answer_set.exists():
#                 category = answer_set.first().category
#                 categories.add(category) 
#                 count[category] = count.get(category, 0) + 1

#         total_answers = len(selected_answers)
#         for category in categories:
#             cnt = count.get(category, 0)
#             percentages[category] = round((cnt / total_answers) * 100) if total_answers > 0 else 0

#         context = {
#             'selected_answers': selected_answers, 
#             'category_counts': count,            
#             'category_percentages': percentages,  
#         }
#         print(percentages)

#         return render(request, 'result.html', context)

#     return render(request, 'result.html', {})








def result(request):

    if request.method == 'POST':
        selected_answers = [value for key, value in request.POST.items() if key.startswith('answer_')]
        print(selected_answers)
        count = {}
        percentages = {}
        categories = set() 

        for answer_text in selected_answers:
            answer_set = Answer.objects.filter(answer_text=answer_text).order_by('-id')
            if answer_set.exists():
                category = answer_set.first().category
                categories.add(category) 
                count[category] = count.get(category, 0) + 1

        total_answers = len(selected_answers)
        for category in categories:
            cnt = count.get(category, 0)
            percentages[category] = round((cnt / total_answers) * 100) if total_answers > 0 else 0

        category_data = [{'name': category.name, 'per': percentages[category]} for category in categories]
        category_data = sorted(category_data, key=lambda x: x['per'], reverse=True) 

        context = {
            'selected_answers': selected_answers,
            'category_data': category_data,  
        }
        print(category_data)

        return render(request, 'result.html', context)

    return render(request, 'result.html', {})

