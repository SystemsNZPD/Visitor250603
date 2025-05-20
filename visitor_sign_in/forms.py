from django import forms
from phonenumber_field.formfields import PhoneNumberField


class VisitorForm(forms.Form): #inherit class Form from forms module
    VISIT_TO_CHOICES = [
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
    phone_number = PhoneNumberField(widget=forms.TextInput(
        attrs={'inputmode': 'numeric', 'pattern': '[0-9]*', 'placeholder': 'Please enter your phone number'}))
    visit_to = forms.ChoiceField(
        max_length=40,
        choices=VISIT_TO_CHOICES,
        help_text="Who are you visiting"
    )
