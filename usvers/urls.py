from django.urls import path
from . import views


import os
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.usvers_home, name='usvers_home'),
    path('usvers_create', views.usvers_create, name='usvers_create'),
    path('<int:pk>', views.UsversDetailView.as_view(), name='usvers_detail'),
  #  path('<int:pk>/update', views.NewUpdateView.as_view(), name='news-update'),
    path('delete/', views.UsversDelete, name='usvers_delete'),
    path('usver_data/', views.UsverData, name='usver_data'),
    path('del/<int:id>/', views.Del),
    path('us_download/doc/<str:FilePath>/', views.some_view),
    path('us_download/images/<str:FilePath>/', views.some_view_images),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
