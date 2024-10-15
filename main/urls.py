from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),

    path('chat/<str:room_name>/', views.room, name='room'),
    path('chat', views.chat, name='chat'),

    path('requests_get', views.requests_get, name='requests_get'),
    path('about_pdf', views.about_pdf, name='about_pdf'),
    path('about_write_pdf', views.about_write_pdf, name='about_write_pdf'),
    path('about_pdf2', views.about_pdf2, name='about_pdf2'),
]
