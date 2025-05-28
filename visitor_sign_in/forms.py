from django import forms
from phonenumber_field.formfields import PhoneNumberField

def validate_digits(value):
    if not value.isdigit():
        raise forms.ValidationError("Please enter digits only (0-9). ")

class VisitorForm(forms.Form): #inherit class Form from forms module
    VISIT_TO_CHOICES = [
        ('', 'Select who you are visiting'),
        ('tony', 'Tony Cox-Smith'),
        ('ann', 'Ann Mansoor'),
        ('joanna', 'Joanna Wu'),
        ('mele', 'Mele Tatafu'),
        ('vicky', 'Weidi Qu'),
        ('emily', 'Emily Donovan'),
        ('ray', 'Ray Lee'),
        ('ricky', 'Richard Light'),
        ('cy', 'Chim Yun Cheng'),
        ('julie', 'Julie Ullness'),
    ]

    visitor_name = forms.CharField(max_length=80)   #database table, character filed
    company_name = forms.CharField(max_length=80)
    phone_number = forms.CharField(
        max_length=20,
        required=True,
        validators=[validate_digits],
        widget=forms.TextInput(attrs={
            'placeholder': 'Please enter your phone number',
            'inputmode': 'numeric',
            'pattern': '[0-9]*'
        })
    )
    visit_to = forms.ChoiceField(
        choices=VISIT_TO_CHOICES,
        # help_text="Who are you visiting"
    )

    has_no_fever = forms.BooleanField(label= "I Have No Fever", required=True)
    has_no_vomiting = forms.BooleanField(label= "I Have No Vomiting or Diarrhoea", required=True)
    has_no_skin_lesions = forms.BooleanField(label= "I Have No Discharging Skin Lesions", required=True)
    has_no_running_nose = forms.BooleanField(label= "I Have No Running Nose or Ear Discharge", required=True)
