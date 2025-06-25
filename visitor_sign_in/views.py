from django.shortcuts import render
from .forms import VisitorForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils import timezone

VISIT_TO_EMAILS = {
    'tony': 'tony.cox-smith@nzpuredairy.co.nz',
    'ann': 'ann.mansoor@nzpuredairy.co.nz',
    'joanna': 'joanna.wu@nzpuredairy.co.nz',
    'mele': 'mele.tatafu@nzpuredairy.co.nz',
    'vicky': 'weidi.qu@nzpuredairy.co.nz',
    'emily': 'emily.donovan@nzpuredairy.co.nz',
    'ray': 'ray.lee@nzpuredairy.co.nz',
    'ricky': 'richard.light@nzpuredairy.co.nz',
    'cy': 'chimyun.cheng@nzpuredairy.co.nz',  # Exceptional case
    'julie': 'julie.ullness@nzpuredairy.co.nz',
}


def index(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor_name = form.cleaned_data["visitor_name"]
            company_name = form.cleaned_data["company_name"]
            phone_number = form.cleaned_data["phone_number"]
            visit_to = form.cleaned_data["visit_to"]
            has_no_fever = form.cleaned_data["has_no_fever"]
            has_no_vomiting = form.cleaned_data["has_no_vomiting"]
            has_no_skin_lesions = form.cleaned_data["has_no_skin_lesions"]
            has_no_running_nose = form.cleaned_data["has_no_running_nose"]

            Form.objects.create(visitor_name=visitor_name,
                                company_name=company_name,
                                phone_number=phone_number,
                                visit_to=visit_to,
                                has_no_fever=has_no_fever,
                                has_no_vomiting=has_no_vomiting,
                                has_no_skin_lesions=has_no_skin_lesions,
                                has_no_running_nose=has_no_running_nose)

            messages.success(request, "Form Submitted successfully!!!")
            form = VisitorForm()  # Clear the form after successful submission
            message_body = f"{visitor_name} From {company_name} is here!"

            #Get the recipient's email based on visit_to
            recipient_email = VISIT_TO_EMAILS[visit_to]
            if recipient_email:
                email_message = EmailMessage(subject="You have Visitor!!",
                                             body=message_body,
                                             to=[recipient_email])
                email_message.send()  #specifiy the sender in setting .py
            else:
                messages.warning(request,"No eamil recipient found for this selection")

        else:
            messages.warning(request, "Form submission failed. Please correct the errors.")
    else:
        form = VisitorForm()
    return render(request, "index.html", {"form": form})

def return_visitor(request):
    # Get all unique companies from the database for the dropdown
    companies = Form.objects.values_list('company_name', flat=True).distinct().order_by('company_name')
    visit_to_choices = Form.VISIT_TO_CHOICES

    # Prepare visitors_by_company for the dropdown logic
    visitors_by_company = {}
    for company in companies:
        visitors = Form.objects.filter(company_name=company).values_list('visitor_name', 'phone_number').distinct()
        visitors_by_company[company] = list(visitors)

    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            # Get cleaned data from the form
            company_name = form.cleaned_data['company_name']
            visitor_name = form.cleaned_data['visitor_name']
            phone_number = form.cleaned_data['phone_number']
            visit_to = form.cleaned_data['visit_to']
            has_no_fever = form.cleaned_data['has_no_fever']
            has_no_vomiting = form.cleaned_data['has_no_vomiting']
            has_no_skin_lesions = form.cleaned_data['has_no_skin_lesions']
            has_no_running_nose = form.cleaned_data['has_no_running_nose']




            # Save to database
            Form.objects.create(
                visitor_name=visitor_name,
                company_name=company_name,
                phone_number=phone_number,
                visit_to=visit_to,
                has_no_fever=has_no_fever,
                has_no_vomiting=has_no_vomiting,
                has_no_skin_lesions=has_no_skin_lesions,
                has_no_running_nose=has_no_running_nose
            )



            messages.success(request, "Return visitor sign-in submitted successfully!")
            message_body = f"{visitor_name} From {company_name} is here!"

            recipient_email = VISIT_TO_EMAILS[visit_to]
            email_message = EmailMessage(subject="You have Visitor!!",
                                         body=message_body,
                                         to=[recipient_email])
            email_message.send()  # specifiy the sender in setting .py

            form = VisitorForm()  # Clear the form after successful submission
        else:
            messages.warning(request, "Form submission failed. Please correct the errors.")
    else:
        form = VisitorForm()

    context = {
        'companies': companies,
        'visitors_by_company': visitors_by_company,
        'visit_to_choices': visit_to_choices,
        'form': form,  # Pass the form for error display if needed
    }
    return render(request, 'return_visitor.html', context)

def choose_visitor(request):
    return render(request, 'choose_visitor.html')

def sign_out_view(request):
    if request.method == 'POST':
        visitor_id = request.POST.get('visitor_id')
        try:
            visitor = Form.objects.get(id=visitor_id, sign_out__isnull=True)
            visitor.sign_out = timezone.now()
            visitor.save()
            # Show success message and redirect after 5 seconds
            return render(request, 'sign_out.html', {
                'success': True,
                'visitor_name': visitor.visitor_name,
            })
        except Form.DoesNotExist:
            # Handle not found or already signed out
            return render(request, 'sign_out.html', {
                'error': "Visitor not found or already signed out.",
                'visitors': Form.objects.filter(sign_out__isnull=True)
            })
    else:
        # GET: show dropdown
        visitors = Form.objects.filter(sign_out__isnull=True).order_by('-created_at')
        return render(request, 'sign_out.html', {'visitors': visitors})