from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForms
from django.views.generic import DetailView, UpdateView, DeleteView

#Для таймера
from django.utils import timezone
from datetime import timedelta

import time
import threading

#Для таблицы
from .tables import ArticlesTable
from django_tables2 import RequestConfig

#Для логирования
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin




@login_required
def news_home(request):
   #delay = 5  # время между вызовами функции в секундах, в данном примере - 5 c
   # while True:
   #time.sleep(delay)
   #redirect(request)
   # вызываемая в отдельном потоке функция в ней и производим действия из следующего шага
   # thread = threading.Thread(target=news_home, args=(request,))
   # thread.start()
   #print(request)

   # Проверяем есть ли у данного пользователя разрешение для просмотра
   # Если такого разрешения нет, то выкидываем исключение PermissionDenied
    if not request.user.has_perm('news.view_articles'):
       raise PermissionDenied

    news = Articles.objects.all()
    #news = Articles.objects.order_by('title')
    Time=timezone.now()+timedelta(hours=5)
    #Time=Time+timedelta(seconds=60)
    Time=Time.strftime("%a %d-%m-%Y %H:%M:%S")
    data={
        'news': news,
        'Time': Time,
    }
    return render(request, 'news/news_home.html', data)


def news_home_tables(request):
    table = ArticlesTable(Articles.objects.all())
    RequestConfig(request).configure(table)

    data={
        'table': table,
    }
    return render(request, 'news/news_home_tables.html', data)


class NewDetailView(PermissionRequiredMixin, DetailView):
#только тому пользователю у которого есть просмотр доступ
 permission_required = 'news.change_articles'
 model=Articles
 template_name = 'news/detail_views.html'
 context_object_name = 'new_article'




class NewUpdateView(PermissionRequiredMixin, UpdateView):
    # только тому пользователю у которого есть просмотр доступ
    permission_required = 'news.change_articles'
    model = Articles
    template_name = 'news/create.html'
    #context_object_name = 'UpdateView'
    #fields = ['title','anons','full_text','date']
    form_class = ArticlesForms



class NewDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


@login_required
#только тому пользователю у которого есть добавление доступ
@permission_required('news.add_articles', raise_exception=True)
def create(request):
    error=''
    if request.method == 'POST':
        form = ArticlesForms(request.POST)
        if form.is_valid():
            #title = form.cleaned_data["title"]
            #print(title)
            form.save()
            return redirect('home')
        else: error='Ошибка формы'


    form= ArticlesForms()
    data={
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)

  # Таймер
def do_news_taimer(request):
    delay = 3  # время между вызовами функции в секундах, в данном примере - 1 c
    #print(request)
    while True:
        time.sleep(delay)
        redirect('news_home')
        print("Отправил 4")
        #news_home('/news/')
        # вызываемая в отдельном потоке функция в ней и производим действия из следующего шага
        #thread = threading.Thread(target=do_news_taimer, args=("/",))
        #thread.start()

    pass

