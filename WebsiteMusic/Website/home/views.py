from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def home(request):
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render())

def main1(request):
    template = loader.get_template('main1/main1.html')
    return HttpResponse(template.render())

def main2(request):
    template = loader.get_template('main2/main2.html')
    return HttpResponse(template.render())

@csrf_exempt
def save_text(request):
    if request.method == 'POST':
        text_input = request.POST.get('textInput', '')

        if text_input:
            filename = 'considering.txt'
            file_path = os.path.join(os.path.dirname(__file__), filename)

            with open(file_path, 'a') as file:
                file.write(text_input + '\n')
            # Send an email with the text_input
            send_email(text_input)

        return render(request, 'save_text/save_text.html')
    



def send_email(text_input):
    # Configure your email settings
    smtp_server = 'smtp.gmail.com'  # Gmail SMTP server
    smtp_port = 587  # Gmail SMTP port
    sender_email = 'rushabh02@gmail.com'  # Your Gmail email address
    sender_password = 'pdaofgoyxeavahem'  # Your Gmail password
    receiver_email = 'rushabh02@gmail.com'  # The recipient's email address

    # Create a message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Text Input from Your Website'

    # Attach the text_input to the email
    msg.attach(MIMEText(text_input, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", str(e))

# Make sure to replace 'your_email@gmail.com' and 'your_password' with your actual Gmail credentials.