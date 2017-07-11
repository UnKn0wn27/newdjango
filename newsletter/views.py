from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from .models import SignUp

def home(request):
    title = 'Sign Up Now'
    form = SignUpForm(request.POST or None)
    #add a form
    context = {
        "title": title,
        "form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = 'New full name'
        instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank You"
        }
    if request.user.is_authenticated() and request.user.is_staff:
        #print(SignUp.objects.all())
        # i = 0
        # for instance in SignUp.objects.all():
        #     print(i)
        #     print(instance.full_name)
        #     i+=1
        queryset = SignUp.objects.all().order_by('-timestamp')
        context = {
            "queryset":  queryset
        }

    return render(request, "home.html", context)

def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'yourotheremail@email.com']
        contact_message = "%s: %s via %s"%(form_full_name, form_message, form_email)

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=True )
    context = {
        "form": form,
        "title": title,
    }

    return render(request, "forms.html", context)