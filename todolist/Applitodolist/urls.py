from django.urls import path
from . import views

app_name = 'Applitodolist'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:task_id>/', views.show, name = 'show'),
    path('task/', views.create_task, name = 'create_task')
    #path('login/', views.login, name = 'login' ),
    #path('sign_up/', views.sign_up, name = 'sign_up'),
    #path('form/', views.show_form, name = 'show_form'),
    #path('succ/', views.succ, name = "succ")
    
    #path('submit/', views.submit_form, name= 'submit_form')
]