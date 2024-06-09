from requests import Response
from django.shortcuts import render
from django.core.mail import mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/email.html', context={'from_name': 'Fab', 'to_name': 'Roman'})
        message.attach_file('playground/static/images/Beach.jpeg')
        message.send(['roman@gmail.com'])
    except BadHeaderError:
        return Response('Bad header')
    return render(request, 'hello.html', {'name': 'Fab'})
