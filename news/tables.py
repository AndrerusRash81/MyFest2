import django_tables2 as tables
from .models import Articles

class ArticlesTable(tables.Table):
    #title          = tables.TemplateColumn(attrs={'th':{'style':'width:18%;'}}, template_name='standard/columns/lot_name.html')
    title          = tables.Column(attrs={'th': {'style': 'width:18%;'}})
    full_text      = tables.Column(attrs={'th':{'style':'width:20%;'}})
    date           = tables.DateTimeColumn(attrs={'th':{'style':'width:10%;'}})
    avtor          = tables.Column(attrs={'th':{'style':'width:10%;'}})


    class Meta:
        model = Articles
       # template_name = 'django_tables2/bootstrap4.html'
        attrs = {'class': 'paleblue'}
        empty_text = 'Новости через таблицу'
        fields = ("title","full_text","date","avtor",)