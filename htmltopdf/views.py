from django.http import HttpResponse
from django.shortcuts import render

from htmltopdf.utils import html_to_pdf

context = {
    'data': {
        'name': "Test Name",
        'phone': "+998991234567",
    }
}


def home(request):
    return render(request=request, template_name='index.html', context=context)


def generate_pdf(request):
    pdf = html_to_pdf('index.html', context=context)
    return HttpResponse(pdf, content_type='application/pdf')
