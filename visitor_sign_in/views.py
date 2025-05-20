from django.shortcuts import render
from .forms import VisitorForm


def index(request):
    messages = []
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            # Save or process form.cleaned_data here
            messages.append("Form submitted successfully!")
            form = VisitorForm()  # Clear the form after successful submission
        else:
            messages.append("Form submission failed. Please correct the errors.")
    else:
        form = VisitorForm()
    return render(request, "index.html", {"form": form, "messages": messages})