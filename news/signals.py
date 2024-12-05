from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Articles

#подключаем каналы веб сокета
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
@receiver(post_save, sender=Articles)
#Декоратор @receiver подключает функцию new_create к сигналу post_save модели Articles.
def new_create(sender, instance, created, **kwargs):
    print("------Сигнал------")
    if created:
        #instance: экземпляр модели  Articles, который  был  сохранен.
        title = instance.title
        room = 'chat_%s' % str(instance.room)
        print("Отправка сообщения в комнату "+room)
        #Отправим в комнату сообщение
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(room,
             {
            'type':'my_chat_message',
            'message':'{"msg":"УРА!!!","new":"%s"}' % (str(title)),
            }
        )