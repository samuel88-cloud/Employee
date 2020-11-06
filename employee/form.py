from django import forms
from .models import Employee

from django.forms import ModelForm
from django.contrib import messages
from django.core.exceptions import ValidationError



class EmployeeForm(ModelForm):
    class Meta:
        model= Employee
        fields= ['age']

    # def clean(self):
    #     print(self.cleaned_data.get('name'))
    #     name = self.cleaned_data.get('name')
    #     if name is not None:
    #         super(EmployeeForm,self).clean()
    #     else:
    #         print('eror')
    #         raise ValidationError(
    #                 "Did not send for 'help' in the subject despite "
    #                 "CC'ing yourself."
    #             )
            