from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from data.models import  User

class StudentSignUpForm(UserCreationForm):
    
    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user