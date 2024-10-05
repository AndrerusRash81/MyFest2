from django.db import models
from django.utils import timezone
from django.conf import settings
import os


class BDROL(models.Model):
    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Роль'
        verbose_name_plural='Роли'


class BDUsvers(models.Model):
    name = models.CharField('Название', max_length=50, default='Название')
    rol = models.ForeignKey(BDROL, on_delete=models.SET_NULL, null=True)
    #rol= models.ManyToManyField(BDROL)
    #rol = models.CharField('Роль', max_length=50, default='Роль')
    full_text = models.TextField('Описание')
    activ = models.BooleanField('Активный')
    kesh = models.IntegerField('Наличность')
    date = models.DateTimeField(default=timezone.now)
    infa = models.FileField(upload_to='doc/', null=True, blank=True)
    cover = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'/usvers/{self.id}'

    def get_absolute_url(self):
        return self.name

    def get_All_Summ(self):
        sum=999
        return sum

    def get_infa_name(self):
        filename = os.path.basename(self.infa.name)
        return filename




    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'
