from django.urls import path
from . import views

app_name = 'Applitodolist'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:task_id>/', views.show, name = 'show'),
    path('task/', views.create_task, name = 'create_task')
]