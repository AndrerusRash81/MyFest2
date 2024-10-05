from django.db import models


class Avtor(models.Model):
    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.name

    class Meta:
        verbose_name='Автор'
        verbose_name_plural='Авторы '

class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='ТЕКСТ')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    avtor = models.OneToOneField(Avtor, on_delete = models.CASCADE, null=True, blank=True)

    Status_News_CHOICES=[
        ("TOP","Горячие"),
        ("COOL","Холодные"),
        ("Netral","Нейтральные"),
    ]

    status = models.CharField(max_length=7, choices=Status_News_CHOICES, default="Netral")

    def __str__(self):
        return f'/news/{self.id}'

    def get_absolute_url(self):
        return self.title

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'