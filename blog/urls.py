from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),
    path('update/<int:id>/', views.article_update, name='article_update'),
    path('delete/<int:id>/', views.article_delete, name='article_delete'),
]
