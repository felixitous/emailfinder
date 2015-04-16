from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from validate_email import validate_email
import random

def index(request):
    # test_list = []
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            jank_test = ['felixliu@berkeley.edu']
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            domain_name = form.cleaned_data['domain_name']
            test_list = permutations(first_name, middle_name, last_name, domain_name)
            valid_list = ['']
            return render(request, 'index.html', {'form': form, 'permutations': test_list, 'valid': valid_list})
    else:
        form = NameForm()
    return render(request, 'index.html', {'form': form})

# def valid_or_not(test_list):
#     valid_emails = []
#     for email in test_list:
#         # if validate_email(email):
#         #     valid_emails.append(email)
#         valid_emails.append(validate_email(email, check_mx=True))   
#     return valid_emails

def permutations(first_name, middle_name, last_name, domain_name):
    domain_name = '@' + domain_name
    test_list = []
    #first name
    test_list.append(first_name + domain_name)
    #last name
    test_list.append(last_name + domain_name)

    test_list.append(first_name + last_name + domain_name)
    test_list.append(first_name + '.' + last_name + domain_name)
    test_list.append(first_name[0] + last_name + domain_name)
    test_list.append(first_name[0] + '.' + last_name + domain_name)
    test_list.append(first_name + last_name[0] + domain_name)
    test_list.append(first_name + '.' + last_name[0] + domain_name)
    test_list.append(first_name + '.' + last_name[0] + domain_name)
    test_list.append(first_name[0] + last_name[0] + domain_name)
    test_list.append(first_name[0] + '.' + last_name[0] + domain_name)
    test_list.append(last_name + first_name + domain_name)
    test_list.append(last_name + '.' + first_name + domain_name)
    test_list.append(last_name + first_name[0] + domain_name)
    test_list.append(last_name + '.' + first_name[0] + domain_name)
    test_list.append(last_name[0] + first_name + domain_name)
    test_list.append(last_name[0] + '.' + first_name + domain_name)
    test_list.append(last_name[0] + '.' + first_name + domain_name)
    test_list.append(last_name[0] + first_name[0] + domain_name)
    test_list.append(last_name[0] + '.' + first_name[0] + domain_name)
    test_list.append(last_name[0] + '.' + first_name[0] + domain_name)
    test_list.append(first_name + '-' + last_name + domain_name)
    test_list.append(first_name[0] + '-' + last_name + domain_name)
    test_list.append(first_name + '-' + last_name[0] + domain_name)
    test_list.append(first_name[0] + '-' + last_name[0] + domain_name)
    test_list.append(last_name + '-' + first_name + domain_name)
    test_list.append(last_name + '-' + first_name[0] + domain_name)
    test_list.append(last_name[0] + '-' + first_name + domain_name)
    test_list.append(last_name[0] + '-' + first_name[0] + domain_name)
    test_list.append(first_name + '_' + last_name + domain_name)
    test_list.append(first_name[0] + '_' + last_name + domain_name)
    test_list.append(first_name + '_' + last_name[0] + domain_name)
    test_list.append(first_name[0] + '_' + last_name[0] + domain_name)
    test_list.append(last_name + '_' + first_name + domain_name)
    test_list.append(last_name + '_' + first_name[0] + domain_name)
    test_list.append(last_name[0] + '_' + first_name + domain_name)
    test_list.append(last_name[0] + '_' + first_name[0] + domain_name)

    if middle_name:
        test_list.append(first_name[0] + middle_name[0] + last_name + domain_name)
        test_list.append(first_name[0] + middle_name[0] + '.' + last_name + domain_name)
        test_list.append(first_name + middle_name[0] +  last_name + domain_name)
        test_list.append(first_name + '.' + middle_name[0] + '.' + last_name + domain_name)
        test_list.append(first_name + middle_name + last_name + domain_name)
        test_list.append(first_name + '.' + middle_name + '.' + last_name + domain_name)
        test_list.append(first_name[0] + middle_name[0] + '-' + last_name + domain_name)
        test_list.append(first_name + '-' + middle_name[0] + '-' + last_name + domain_name)
        test_list.append(first_name + '-' + middle_name + '-' + last_name + domain_name)
        test_list.append(first_name[0] + middle_name[0] + '_' + last_name + domain_name)
        test_list.append(first_name + '_' + middle_name[0] + '_' + last_name + domain_name)
        test_list.append(first_name + '_' + middle_name + '_' + last_name + domain_name)

    return test_list
