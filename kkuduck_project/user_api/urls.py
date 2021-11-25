from . import views
from django.urls import path

app_name = 'user_api'

urlpatterns = [
    path('', views.UserView.as_view()),
    path('<int:user_id>', views.UserView.as_view()) #data 바로 밑 id 를 uid라고 하려고 했다가 user_id로 다시 변경, user의 primary key의 id가 전달되는 경우
]


