from django.urls import path
from . import views

app_name = 'Applitodolist'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:task_id>/', views.show, name = 'show'),
    path('supprimer/<int:task_id2>/', views.remove_task, name = 'remove_task'),
    path('task/', views.create_task, name = 'create_task'),
    path('infouser/', views.info_user, name = 'info_user')
]