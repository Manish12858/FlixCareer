from django import forms

from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        # fields=['first_name','last_name','email']
        fields='__all__'

        # customizing labels and error message they are optional
        labels={
            'first_name':_("Enter first name"),
            'last_name':_("Enter your last name"),
            "email":_("Enter email")
        }

        error_messages={
            'first_name':{
            'required':_('you cannot move forword without first name')
            }
        }

        
        # help_texts={'first_name':_('Enter character only')}

# custom validator

# def validate_comm(value):
#     if ',' in value:
#         raise forms.ValidationError("Invalid Last Name")
#     return value

# class SubscribeForm(forms.Form):
#     first_name=forms.CharField(max_length=100,label="Enter First name",help_text="enter character only")
#     last_name=forms.CharField(max_length=100,required=False,disabled=False,validators=[validate_comm])
#     email=forms.EmailField(max_length=100)

    # def clean_first_name(self):
    #     data=self.cleaned_data['first_name']
    #     if "," in data:
    #         raise forms.ValidationError("Invalid First Name")
    #     return data
