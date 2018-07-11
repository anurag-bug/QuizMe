from django import forms
from django.forms import ModelForm,Textarea
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

mychoice=(('A','A'),('B','B'),('C','C'),('D','D'))
class signupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

        def save(self, commit=True):
            user = super(signupForm, self).save(commit=False)

            user.email=cleaned_data['email']

            if commit:
                user.save()

            return user

class QuizCreationForm(ModelForm):
    class Meta:
        model=models.QuizDetails
        fields= ['question','optionA','optionB','optionC','optionD','correctOption']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'optionA': forms.Textarea(attrs={'rows': 2, 'cols': 15}),
            'optionB': forms.Textarea(attrs={'rows': 2, 'cols': 15}),
            'optionC': forms.Textarea(attrs={'rows': 2, 'cols': 15}),
            'optionD': forms.Textarea(attrs={'rows': 2, 'cols': 15}),
        }
class ResponseForm(ModelForm):
    class Meta:
        model=models.ResultLive
        fields=['response','rollNo']
        widgets={
            'response':forms.RadioSelect
        }
