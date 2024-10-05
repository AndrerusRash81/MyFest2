from django.shortcuts import render, redirect
from .models import BDUsvers
from .forms import BDUsversForms
from django.views.generic import DetailView, UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db.models import Sum, Avg, Max, Count
from django.http import FileResponse




def usvers_home(request):
    Usvers = BDUsvers.objects.all()
    UsverssSum = Usvers.aggregate(Usverss_Sum=Sum('kesh'))
    UsversMax = Usvers.aggregate(Мое_Имя_Для_Мах=Max('kesh'))
    UsversAvg = Usvers.aggregate(Avg('kesh'))
    UsversCount = Usvers.annotate(Count('name'))

    #print("----")
    if request.method == 'POST':
        filtrname = request.POST.get('myInput')
        #print(filtrname)
        Usvers = BDUsvers.objects.filter(name__startswith=filtrname)

    data={
        'Usvers': Usvers,
        'UsverssSum': UsverssSum['Usverss_Sum'],
        'UsversMax': UsversMax,
        'UsversAvg': UsversAvg,
        'UsversCount': UsversCount,
    }
    return render(request, 'usvers/usvers_home.html',data)

def usvers_create(request):
    error=''
    if request.method == 'POST':
        form = BDUsversForms(request.POST,request.FILES)
        #kesh=form.cleaned_data.get("kesh")
        kesh_= int(request.POST.get('kesh'))
        print(kesh_)
        name_ = request.POST.get('name')
        print(name_)
        full_text_ = request.POST.get('full_text')
        print(full_text_)
        activ_ = request.POST.get('activ')
        print(activ_)
        date_ = request.POST.get('date')
        print(date_)


        if request.FILES:
        # получаем загруженный файл
          file = request.FILES['myfile']
          print('Name:'+file.name)
          fileIMG = request.FILES['mypict']
          print('Фаул картинки: '+fileIMG.name)
          fs = FileSystemStorage()
        # сохраняем на файловой системе
          filename = fs.save('doc/'+file.name, file)
          filenameIMG = fs.save('images/' + fileIMG.name, fileIMG)
        #  print('filename: ' + filename)
        # получение адреса по которому лежит файл
        #  file_url = fs.url(filename)
        #  print('URL: '+file_url)
          BDUsvers.objects.create(name="Зверь-"+name_, full_text=full_text_, activ=True, kesh=kesh_, date=date_, infa=filename, cover=filenameIMG)
          return redirect('home')


        if kesh_ < 5000:
            error = 'мало положил бабла'
        else:
          if form.is_valid():
            form.save()
            return redirect('home')
          else: error=form.errors



    form= BDUsversForms()
    data={
        'form': form,
        'error': error,
    }
    return render(request, 'usvers/usvers_create.html', data)

class UsversDetailView(DetailView):
    model=BDUsvers
    template_name = 'usvers/detail_views_usvers.html'
    context_object_name = 'US_article'


def UsversDelete(request):
    print('000-000')
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        print(f'номер строки {id}')
        try:
          # Пытаемся найти запись
          #instance = BDUsvers.objects.get(pk=id)
          instance=BDUsvers.objects.filter(pk=id)
          # Если нашли – удаляем
          instance.delete()
          #messages.success(request, 'Запись  успешно удалена. Нотируем это событие.')
        except BDUsvers.DoesNotExist:
          messages.error(request, 'Запись не найдена. Возможно, она уже удалена.')
    return redirect('usvers_home')

# удаление данных из бд
def Del(request, id):
    try:
        person = BDUsvers.objects.get(id=id)
        person.delete()
        return redirect('usvers_home')
    except person.DoesNotExist:
        return redirect('usvers_home')

def UsverData(request):
    if request.method == 'POST':
        Txt = request.POST.get('myInputData')
        print(f'текскт {Txt}')
        try:
         file=open('text.txt','w')
        except ValueError:
         print("error - ")
        except ZeroDivisionError:
         print("error - ")
        else:
         file.write('Привет1\n')
         file.write(Txt)
        finally:
         file.close()

    return redirect('usvers_home')


#Если картинку получаешь как байты:
def some_view_images(request,FilePath):
    buffer = io.BytesIO()
    buffer.write(picture_content)
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="images/doc/"+FilePath)

#Если файл
def some_view(request,FilePath):
    print("Скачивание файла "+FilePath)
    return FileResponse(open("media/doc/"+FilePath,'rb'))

