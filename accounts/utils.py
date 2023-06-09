from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.http.response import HttpResponse

def detectUser(user):
    if user.role == 1:
        redirectUrl = 'Owner'
        return redirectUrl
    elif user.role == 2:
        redirectUrl = 'Vendor'
        return redirectUrl
    elif user.role == 3:
        redirectUrl = 'Agent'
        return redirectUrl
    elif user.role == 4:
        redirectUrl = 'Subagent'
        return redirectUrl
    elif user.role == 5:
        redirectUrl = 'Tenent'
        return redirectUrl                        
    elif user.role == 6:
        redirectUrl = 'Associate'
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'
        return redirectUrl

    
def send_verification_email(request, user, mail_subject, email_template):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    message = render_to_string(email_template, {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    to_email = user.email
    print(from_email)
    print(to_email)
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"
    mail.send()

def send_confirm_email(request, contactus, mail_subject, email_template):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    print(contactus)
    message = render_to_string(email_template, {
        'contactus': contactus,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(contactus.pk)),
        'token': default_token_generator.make_token(contactus),
    })
    to_email = contactus.email
    print(from_email)
    print(to_email)
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"
    mail.send()


def send_notification(mail_subject, mail_template, context):
    from_email = settings.DEFAULT_FROM_EMAIL
    print(context)
    message = render_to_string(mail_template, context)
    if(isinstance(context['to_email'], str)):
        to_email = []
        to_email.append(context['to_email'])
    else:
        to_email = context['to_email']
    mail = EmailMessage(mail_subject, message, from_email, to=to_email)
    mail.content_subtype = "html"
    mail.send()

from django.core.mail import send_mail
def sendmail(request):
    send_mail(
        'NEw SUBSJECT',
        'Email message',
        'aakhan1572@gmail.com',
        ['agsamjad1@gmail.com'],
        fail_silently=False,
        )
    return HttpResponse('Mail successfully sent')


import os
from django.core.files.storage import default_storage
from django.db.models import FileField


def file_cleanup(sender, **kwargs):
    """
    File cleanup callback used to emulate the old delete
    behavior using signals. Initially django deleted linked
    files when an object containing a File/ImageField was deleted.

    Usage:
    >>> from django.db.models.signals import post_delete
    >>> post_delete.connect(file_cleanup, sender=MyModel, dispatch_uid="mymodel.file_cleanup")
    """
    for fieldname in sender._meta.get_fields():
        try:
            field = sender._meta.get_field(fieldname)
        except:
            field = None

    if field and isinstance(field, FileField):
        inst = kwargs["instance"]
        f = getattr(inst, fieldname)
        m = inst.__class__._default_manager
        if (
            hasattr(f, "path")
            and os.path.exists(f.path)
            and not m.filter(
                **{"%s__exact" % fieldname: getattr(inst, fieldname)}
            ).exclude(pk=inst._get_pk_val())
        ):
            try:
                default_storage.delete(f.path)
            except:
                pass