from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            # Store applicant data in the database
            Form.objects.create(first_name=first_name,
                                last_name=last_name,
                                email=email,
                                date=date,
                                occupation=occupation)

            # Render a success message in the browser
            success_message = f"Thanks for your application, {first_name} {last_name}!"
            messages.success(request, success_message)

            # Email success message to the applicant
            message_subject = "Application submission confirmation"
            message_body = f"Thanks for your application, {first_name} {last_name}.\n" \
                           f"We'll be in touch soon."
            email_message = EmailMessage(message_subject, message_body, to=[email])
            email_message.send()

    return render(request, "index.html")
