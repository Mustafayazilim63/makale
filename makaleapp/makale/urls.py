from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('bugün/', views.bugün, name='bugün'),
    path('sözlük/', views.sözlük, name='sözlük'),
    path('daha/', views.daha, name='daha'),
    path('bir_fikrim_var/', views.bir_fikrim_var, name='bir_fikrim_var'),
]

