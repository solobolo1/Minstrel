from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
from django.views.decorators.csrf import csrf_protect, csrf_exempt

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

        return render(request, 'save_text/save_text.html')