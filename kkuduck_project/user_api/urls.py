from . import views
from django.urls import path

app_name = 'user_api'

urlpatterns = [

    # User_view
    path('', views.UserView.as_view()), #User에 관한 API를 처리하는 view로 Request를 넘김
    path('<int:user_id>', views.UserView.as_view()), #data 바로 밑 id 를 uid라고 하려고 했다가 user_id로 다시 변경, user의 primary key의 id가 전달되는 경우

    # DefaultSubscription_view
    path('', views.DefaultSubView.as_view()),
    path('<str:plan_name>', views.DefaultSubView.as_view()),

    # Subscription_view
    path('', views.SubView.as_view()),
    path('<str:plan_name>', views.SubView.as_view())


]


