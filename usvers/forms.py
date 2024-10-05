from django import forms
from .models import BDUsvers
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, CheckboxInput, IntegerField, FileInput
from datetime import datetime, date, time


class BDUsversForms(ModelForm):
    class Meta:
        model=BDUsvers
        fields=['name', 'rol', 'full_text', 'activ', 'kesh', 'date', 'infa', 'cover']

        widgets={
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название пользователя' }),

            #"rol": TextInput(attrs={
            #    'class': 'form-control',
            #    'placeholder': 'Роль пользователя'}),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание пользователя'}),

            #"activ": CheckboxInput(attrs={
            #    'class': 'form-control',
            #    'placeholder': 'Активный'}),

            "kesh": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наличность'}),

            #"date": DateTimeInput(attrs={
            #    'type': 'date-time',
            #    }),
            "date": forms.DateTimeInput(format='%d.%m.%Y %H:%M', attrs={'class':'form-control'}),


        }
