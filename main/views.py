from django.shortcuts import render, redirect
from django.http import HttpResponse

#Запросы к сайтам
import json
import requests

#Для pdf
import os
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
#from io import
from django.contrib.staticfiles import finders

#2 вариант
#from weasyprint import HTML
#from django.template.loader import render_to_string
from io import BytesIO

def index(request):
      return render(request,'main/index.html')


def about(request):
 #   return HttpResponse("<h4>Проверка Работы about!!!  <h4>")
   return render(request, 'main/about.html')

def requests_get(request):
    URL = 'http://cl.tsst.kz/api'
    wallets_read = URL + '/wallets/'

    username = 'admin@gmail.com'
    password = '!1Asdwer'
    idn=""

    url = wallets_read + idn
    #response = requests.get(headers={'Content-Type': 'application/json'}, url=url, verify=False,auth=HTTPBasicAuth(username, password))
    #info = json.loads(response.text)

    response = requests.get(headers={'Content-Type':'application/json'}, url='https://httpbin.org/get')
    print("----content-----")
    print(response.content)
    print("----text----")
    print(response.text)

    info=response.json()
    print("----json------")
    print(info)

    info=json.loads(response.text)
    print("----json.loads(response.text)-----")
    print(info)

    info=response.headers
    print("----headers----")
    print(info)

    info=response.headers.get('Server')
    print("----headers.get('Server')----")
    print(info)

    data = {
        'info':info
    }
    return render(request, 'main/requests_get.html', data)

#Работа с PDF
def fetch_pdf_resources(uri, rel):
    if uri.find(settings.MEDIA_URL) != -1:
        path = os.path.join(settings.MEDIA_ROOT,  uri.replace(settings.MEDIA_URL,  ''))
    elif uri.find(settings.STATIC_URL) != -1:
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
    else:
        path = None
    print("------>")
    print(path)
    return path

def link_callback(uri, _rel):
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = [os.path.realpath(path) for path in result]
        path = result[0]
    else:
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

def about_pdf(request):
    #response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="Отчет.pdf"'
    template = get_template('main/pdfdoc.html')
    html_ = template.render({
        'lot': 1,
        'position': 2,
        'applications':3
    })
    result = BytesIO()
    pisaStatus = pisa.CreatePDF(
        BytesIO(html_.encode("UTF-8")),
        dest=result,
        encoding='UTF-8',
        link_callback=fetch_pdf_resources
    )
    #pisaStatus = pisa.pisaDocument(BytesIO(html_.encode('UTF-8')), result, encoding='utf-8',link_callback=fetch_pdf_resources)
    if pisaStatus.err:
        return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisaStatus.err, html_))
    return HttpResponse(result.getvalue(), content_type='application/pdf')

def write_pdf(template_src, filename):
    template = get_template(template_src)
    html_ = template.render({
       'lot': 1,
        'position': 2,
        'applications':3
    })
    result = open(filename, 'wb') # Changed from file to filename
    pdf = pisa.CreatePDF(
        html_.encode("UTF-8"),
        result,
        encoding='utf-8',
        link_callback=fetch_pdf_resources)
    result.close()
    if not pdf.err:
        pisa.startViewer(filename)
    pass

def about_write_pdf(request):
    template_src='main/pdfdoc.html'
    filename="FileMyPDF.pdf"
    write_pdf(template_src, filename)
    return redirect('about')

#2 вариант
def about_pdf2(request):
    #   memory_buffer = BytesIO()
    #   template_src = 'main/pdfdoc.html'
    #   context = {
    #      'lot': 1,
    #       'position': 2,
    #       'applications':3
    #   }
    #   html_content = render_to_string(template_src, context)
    #   pdf = HTML(string=html_content).write_pdf(target=memory_buffer)
    #
    #   response = HttpResponse(memory_buffer.getvalue(), content_type='application/pdf')
    #
    #   return response
    return redirect('about')


