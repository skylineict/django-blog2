from django import forms
from django.core.exceptions import ValidationError
# from .form import Signup
#

# def email_comf(value):
# emailcheck = Signup.email
# comfirm = Signup.comfirm_email
# if emailcheck and comfirm not in value:
# raise forms.ValidationError('email no he same')

#


def blacklist(value):
    emaillist = ["@gmail.com", "@yahoo.com"]
    for list in emaillist:
        if list in value:
            raise forms.ValidationError('this email not allow')


# def emailvalue(value, self):
    # data = super(Signup, self)
    # email = self.cleaned_data.get('email')
    # comfirm_email = self.cleaned_data.get('comfirm_email')
    # if email.value != email.value:
        # raise forms.ValidationError("value most be 6 charatesr")
