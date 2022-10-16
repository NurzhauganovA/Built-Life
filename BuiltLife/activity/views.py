from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Company


def CreateCompany(request):
    goals = Company.GOAL_CHOICES
    result = []
    for goal in goals:
        for i in goal:
            result.append(i)
    get_more_visitors = result[0]
    get_more_money = result[2]
    get_more_messages = result[4]
    get_more_likes = result[6]

    context = {
        'get_more_visitors': get_more_visitors,
        'get_more_money': get_more_money,
        'get_more_messages': get_more_messages,
        'get_more_likes': get_more_likes
    }

    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        company_logo = request.POST.get('company_logo')
        company_goal = request.POST.get('goal_role')
        company_email = request.POST.get('company_email')
        company_phone_number = request.POST.get('company_phone_number')
        company_description = request.POST.get('company_description')
        company_address = request.POST.get('actual_address')
        company_address_second = request.POST.get('actual_address_second')
        company_city = request.POST.get('city_actual_address')
        company_post_code = request.POST.get('post_code_actual_address')

        if company_name is None or company_name == '':
            return redirect('create_company')
        elif company_email is None or company_email == '':
            return redirect('create_company')
        elif company_phone_number is None or company_phone_number == '' or company_phone_number.isalpha():
            return redirect('create_company')
        elif company_address is None or company_address == '':
            return redirect('create_company')
        elif company_city is None or company_city == '' or company_city.isnumeric():
            return redirect('create_company')
        elif company_post_code is None or company_post_code.isalpha():
            return redirect('create_company')
        elif company_logo is None:
            return redirect('create_company')

        if company_name is not None and company_post_code.isnumeric():
            Company.objects.create(
                company_name=company_name,
                company_logo=company_logo,
                company_goal=company_goal,
                company_description=company_description,
                company_email=company_email,
                company_phone_number=company_phone_number,
                company_address=company_address,
                company_address_second=company_address_second,
                company_city=company_city,
                company_post_code=company_post_code
            )
            print('Company created')
            messages.success(request, 'Company successfully created')
            return redirect('/')

    return render(request, 'activity/create_company.html', context)


def CreateActivity(request):
    return render(request, 'activity/create_activity.html')