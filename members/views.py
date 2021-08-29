from django import forms
from django.db import connection, connections
from django.forms.forms import Form
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.urls.base import is_valid_path, reverse
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from members.form import Contactusform, Signup
from django.contrib.auth import login, authenticate
from .models import Contactus
from django.core.mail import mail_admins, message, send_mail, BadHeaderError, send_mass_mail
from blog.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, get_connection
from singup.form import UserCreationForm, UserChangeForm
from django.core import mail

# Create your views here.
#
#


class Registration(CreateView):

    form_class = Signup
    template_name = "registration/register.html"
    success_url = reverse_lazy("home")


#


# class Editprofile(UpdateView):

#     form_class = UserChangeForm
#     context_object_name = 'forms'
#     template_name = "registration/editprofile.html"
#     success_url = reverse_lazy("home")

#     def get_object(self):
#         return self.request.user


class Conactme(CreateView):
    form_class = Contactusform
    context_object_name = "forms"
    template_name = "registration/contactus.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            purpose = form.cleaned_data['purpose']
            phone = form.cleaned_data['phone']
            comment = form.cleaned_data['comment']
            form.save()
        content = {"fullname": full_name,
                   "phone":  phone,
                   "purpose": purpose
                   }

        # def mail_admins(subject, message, fail_silently=False, connection=None, html_message=None):
        # send = mail_admins("subject", "admin", fail_silently=False)
        # if send:
        # return HttpResponse('message sent ')
        # else:
        # return HttpResponse("mesaage not sent to")
        userssubject = "Users Registrations"
        adminsubject = "Welcome message"
        html_message = render_to_string(
            template_name="emails/email_comfirmation.html", context=content)
        meg = EmailMultiAlternatives(
            adminsubject, full_name, EMAIL_HOST_USER, [email])
        meg.attach_alternative(html_message, 'text/html')
        meg.send()
        registration = comment + \
            ': full_name: {},phone: {}, purpose{}'.format(
                full_name, phone, purpose)
        subject = "Users Registrations"
#
        # smsme= mail.EmailMultiAlternatives(userssubject,
        #    EMAIL_HOST_USER, [EMAIL_HOST_USER])
        # mesg.attach_alternative(html_message, 'text/html')
        # mesg.send()
        send_mail(subject=subject, message=registration, from_email=EMAIL_HOST_USER, recipient_list=[EMAIL_HOST_USER],
                  fail_silently=False)
        if send_mail:
            return render(self.request, "registration/sucesss.html")
# if send_mail:
# return HttpResponse("mail sent thanks")

        # def mail_admins(subject, message, fail_silently=False, connection=None, html_message=None):
        # send = mail_admins("subject", "admin", fail_silently=False)
        # if send:
        # return HttpResponse('message sent ')
        # else:
        # return HttpResponse('not sent')

        # mail_admins("subject", "admin", fail_silently=False)
        # send = mail_admins("subject", "admin", fail_silently=False)
        # if send:
        # return HttpResponse('message sent ')
        # if mesg.send:
        # return render(self.request, "registration/sucesss.html")
        # else:
        # return HttpResponse('meassge not sent')

        # def mail_admin(subject, message, fail_silently=False, connection=None, html_message=None):
        # mail_admins("subject", "admin", fail_silently=False)
        # send = mail_admins("subject", "admin", fail_silently=False)

        # send = mail_admins(subject, registration, 'hekk',
        #    fail_silently=False,)
        # if mail_admins:
        # return render(self.request, "registration/sucesss.html")
        # else:
        # return HttpResponse("email no sent")

        # if meg.send:
        # return render(self.request, "registration/sucesss.html")
        # userssubject = "Users Registrations"
        # users = "Welcome message"
        # emai_from = 'skylineict@gmai.com'
        # html_message = render_to_string(
        # template_name="emails/email_comfirmation.html",)
        # from_mail = EMAIL_HOST_USER


# adminmessage = (userssubject, html_message,EMAIL_HOST_USER, [EMAIL_HOST_USER])

        # mail1  =mail.message ( userssubject, EMAIL_HOST_USER, email)
        # mail2  =mail.message ( users, EMAIL_HOST_USER, EMAIL_HOST_USER
#
        # datatuple = (
        # (userssubject, full_name,
        #  from_mail, [from_mail]),
        # (users, html_message, from_mail, [email])
        # )

        # connection = connection or get_connection(
        # username=user, password=password, fail_silently=fail_silently)
        # messages = []
        # for subject, text,  from_email, recipient in datatuple:

        # message = EmailMultiAlternatives(
        # subject, text, from_email, recipient)
        # message.attach_alternative(html_message, 'text/html')
        # messages.append(message)
        # return connection.send_messages(messages)
        # return render(self.request, "registration/sucesss.html")
        # datatuple = (
        # (userssubject, full_name,
        #  from_mail, [from_mail]),
        # (users, html_message, from_mail, [email]),
        # )
#
        # for (userssubject, full_name, from_mail, users,  email) in datatuple:
        # mymessage = EmailMultiAlternatives(
        # userssubject, full_name, from_mail, users, email)
        # mymessage.attach_alternative(html_message, 'text/html')
        # connection.send_messages(mymessage)
        # if connection.send_messages:
        # return render(self.request, "registration/sucesss.html")
        # connection.close()

        # userssubject = "Users Registrations"
        # users = "Welcome message"
        # emai_from = 'skylineict@gmai.com'
        # html_message = render_to_string(
        # template_name="emails/email_comfirmation.html",)
        # adminmessage = (userssubject, html_message,EMAIL_HOST_USER, [EMAIL_HOST_USER])
        # usermessage = (users, html_message,EMAIL_HOST_USER[email])e):

# datatuple = (
        # (userssubject, full_name,
        #  EMAIL_HOST_USER, [EMAIL_HOST_USER]),
        # (adminsubject, html_message, EMAIL_HOST_USER, [email]),)

        # with get_connection() as connection:
        # mess = EmailMultiAlternatives(datatuple)
        # mess.attach_alternative(html_message, 'text/httml')
        # connection = connection
        # mess.send()

        # return render(self.request, "registration/sucesss.html")

        # mesg = mail.EmailMultiAlternatives(
        # userssubject, EMAIL_HOST_USER, [email])
        # mesg.attach_alternative(html_message, 'text/html')
        # con = connection
        # mesg.send()
        # if mesg.send:
        # return render(self.request, "registration/sucesss.html")
#


# class Conactme(CreateView):
    # form_class = Contactusform
    # context_object_name = "forms"
    # template_name = "registration/contactus.html"
    # success_url = reverse_lazy('home')
#
    # def form_valid(self, form):
        # if form.is_valid():
#
#
        # email = form.cleaned_data['email']
        # full_name = form.cleaned_data['full_name']
        # purpose = form.cleaned_data['purpose']
        # phone = form.cleaned_data['phone']
        # comment = form.cleaned_data['comment']
        # form.save()
        # content = {"fullname": full_name,
        #    "phone":  phone,
        #    "purpose": purpose
        #    }
        # userssubject = "Users Registrations"
        # adminsubject = "Welcome message"
        # html_message = render_to_string(
        # template_name="emails/email_comfirmation.html", context=content)
        # meg = EmailMultiAlternatives(
        # adminsubject, full_name, EMAIL_HOST_USER, [email])
        # meg.attach_alternative(html_message, 'text/html')
        # meg.send()
        # if meg.send:
        #  return render(self.request, "registration/sucesss.html")
        # return super(forms).form_valid(form)

        # textmessage = render_to_string(template_name='email_comfirmaion.txt')

        # datatuple = (
        # (userssubject, full_name,
        #  EMAIL_HOST_USER, [EMAIL_HOST_USER]),
        # (adminsubject, html_message, EMAIL_HOST_USER, [email]),
        # )

        # send_mass_mail(datatuple=datatuple)
        # if send_mass_mail:
        # return render(self.request, "registration/sucesss.html")
        # return super(forms).form_valid(form)
#

        #
        # def form_valid(self, form):
        # if form.is_valid():

        # email = form.cleaned_data['email']
        # full_name = form.cleaned_data['full_name']
        # purpose = form.cleaned_data['purpose']
        # phone = form.cleaned_data['phone']
        # comment = form.cleaned_data['comment']
        # form.save()
        # subject = "Notication email"
        # fromemail = EMAIL_HOST_USER
        # to_email = email
        # comment  = comment
#
        # send_mail(subject=subject, message=comment, from_email=fromemail, recipient_list=[to_email],
        #   fail_silently=False)
        # if send_mail:
        # return HttpResponse("mail sent thanks")

        # send_mass_mail((mymessage), fail_silently=False)


def sucess(request):
    return render(request, "registration/sucesss.html")

    # form.save(commit=False)
    # username = form.cleaned_data.get('username')
    # password1 = form.cleaned_data.get('password1')
    # password2 = form.cleaned_data.get('password2')
    # firstname = form.cleaned_data.get('firstname')
    # email = form.cleaned_data.get('email')
    # ciy = form.cleaned_data.get('city')
    # user = form.save()
    # login(request, user)
    # return redirect(reverse('home'))
    # else:
    # form = Signup()
    # return render(request, "registration/register.html", {'form': form})

    # def get_question(request):
    # if request.method == 'POST':
    # form = QuestionPostForm(request.POST)
    # if form.is_valid():
    # obj = QuestionPost()
    # obj.question = form.cleaned_data['question']
    # obj.tag = form.cleaned_data['tag']
    # obj.save()
    # return HttpResponseRedirect('forum/index.html', {'form': form})
    #
    # else:
    # form = QuestionPostForm()
    # return render_to_response(request, 'forum/index.html', {'form': form})
