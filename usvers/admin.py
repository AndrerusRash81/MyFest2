from django.contrib import admin
from .models import BDUsvers, BDROL

class UsversAdmin(admin.ModelAdmin):
    #Определим поля видимости
    list_display = ('name', 'rol', 'activ', 'kesh', 'date')
    #По каким полям фильтр с права
    list_filter = ('name', 'rol', 'kesh')
    # По каким полям фильтр поиск
    search_fields = ('name', 'kesh')

admin.site.register(BDUsvers, UsversAdmin)

admin.site.register(BDROL)
