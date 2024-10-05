from django.contrib import admin
from .models import Articles, Avtor

class ArticlesAdmin(admin.ModelAdmin):
    #Определим поля видимости
    list_display = ('title', 'anons', 'avtor', 'status', 'date')
    #По каким полям фильтр с права
    list_filter = ('title', 'avtor', 'status')
    # По каким полям фильтр поиск
    search_fields = ('title',)

admin.site.register(Articles,ArticlesAdmin )
admin.site.register(Avtor)


