from django.urls import path
from . import views

urlpatterns = [
        path('<str:character1>/<str:character2>/', views.my_novel, name='my_novel_haha')
        ]
