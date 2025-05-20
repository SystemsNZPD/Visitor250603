from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Form(models.Model):
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

    visitor_name = models.CharField(max_length=80)
    company_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    visit_to = models.CharField(
        max_length=40,
        choices=VISIT_TO_CHOICES,
        help_text="Who are you visiting"
    )

    def __str__(self):
        return f"{self.visitor_name} from {self.company_name}"
