from django.shortcuts import render
from .forms import VisitorForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor_name = form.cleaned_data["visitor_name"]
            company_name = form.cleaned_data["company_name"]
            phone_number = form.cleaned_data["phone_number"]
            visit_to = form.cleaned_data["visit_to"]

            Form.objects.create(visitor_name=visitor_name, company_name=company_name,
                                phone_number=phone_number, visit_to=visit_to)

            message_body = f"{visitor_name} From {company_name} is here!"
            email_message = EmailMessage(subject="You have Visitor!!", body=message_body, to=["raylee598@gmail.com"])
            email_message.send()  #specifiy the sender in setting .py

            messages.success(request, "Form Submitted successfully!!!")
            form = VisitorForm()  # Clear the form after successful submission
        else:
            messages.warning(request,"Form submission failed. Please correct the errors.")
    else:
        form = VisitorForm()
    return render(request, "index.html", {"form": form})

def return_visitor(request):
    # Get all unique companies from the database
    companies = Form.objects.values_list('company_name', flat=True).distinct().order_by('company_name')

    visit_to_choices = Form.VISIT_TO_CHOICES

    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        visitor_name = request.POST.get('visitor_name')
        phone_number = request.POST.get('phone_number')
        visit_to = request.POST.get('visit_to')

        #save to database
        Form.objects.create(
            visitor_name=visitor_name,
            company_name=company_name,
            phone_number=phone_number,
            visit_to=visit_to
        )
        messages.success(request, "Return visitor sign-in submitted successfully!")

    # Prepare visitors_by_company for the dropdown logic
    # Get all visitors grouped by company
    visitors_by_company = {}
    for company in companies:
        visitors = Form.objects.filter(company_name=company).values_list('visitor_name', 'phone_number').distinct()
        visitors_by_company[company] = list(visitors)

    context = {'companies': companies, 'visitors_by_company': visitors_by_company,
               'visit_to_choices':visit_to_choices}
    print(list(visitors))
    print(visitors_by_company)
    return render(request, 'return_visitor.html', context)
