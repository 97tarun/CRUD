from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django.forms import ModelForm
from django import forms
from .models import Employee

GENDER_CHOICE=[
    ('Male', 'Male'),
    ('Female', 'Female')
]

CITY_CHOICE=[
    ('Delhi','Delhi'),
    ('Pune','Pune'),
    ('Mumbai','Mumbai'),
    ('Bangalore','Bangalore'),
    ('Hyderabad','Hyderabad'),
    ('Chennai','Chennai'),
    ('Kolkata','Kolkata'),
    ('Chandigarh','Chandigarh'),
    ('Gurgaon','Gurgaon'),

    
]

class EmployeeForm(ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    city=forms.MultipleChoiceField(label='Preferred City',choices=CITY_CHOICE,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model=Employee
        fields=['name','email','password','gender','city', 'resume', 'img']
        labels={'name':'Full Name', 'email':'Email ID', 'resume':'Resume', 'img':'Image'}

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'},render_value=True),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'resume':forms.FileInput(attrs={}),
            'img':forms.FileInput(attrs={})

        }