from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('news_tables', views.news_home_tables, name='news_home_tables'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewDeleteView.as_view(), name='news-delete'),
    path('taimer/', views.do_news_taimer, name='news_taimer'),
    path('read_save_EXSEL', views.read_save_EXSEL, name='read_save_EXSEL'),
    path('news_save_EXSEL', views.news_save_EXSEL, name='news_save_EXSEL'),



]
