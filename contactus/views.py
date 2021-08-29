from django.shortcuts import render, HttpResponse
from .models import Contactmeus
# Create your views here.


def contactus(request):
    if request.method == "POST":
        contact = Contactmeus()  # calling my model contact us class from the model.py and save
        # in a variable call contact
        # thi is my name value from my contact.html
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['firstname']

        # now am calling my contact variable and  the instantce of Contactusme  class
        # than i   equall it to contactus.html value after that i save it
        #
        contact.firstname = firstname
        contact.lastname = lastname
        contact.phone = phone
        contact.Email = email
        contact.subject = subject
        contact.save()
        return HttpResponse("<h2> my contactus save to my database sucessfully</h2>")
    return render(request, "contactus/index.html")
