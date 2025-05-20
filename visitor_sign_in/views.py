from django.shortcuts import render
from .forms import VisitorForm
from .models import Form
from django.contrib import messages

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

            messages.success(request, "Form Submitted successfully!!!")
            form = VisitorForm()  # Clear the form after successful submission
        else:
            messages.warning(request,"Form submission failed. Please correct the errors.")
    else:
        form = VisitorForm()
    return render(request, "index.html", {"form": form})