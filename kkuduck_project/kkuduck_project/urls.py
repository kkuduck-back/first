"""kkuduck_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 기본 url
from django.contrib import admin
from django.urls import path, include

# 추가되는 url
from user_api.views import DefaultSubView
from user_api.views import SubView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user_api.urls'), name='user_api'), # from user_api 라는 '앱'에서 import views

    # default_subscription 과 subscription url로 볼 수 있게...
    path('default_subscription/', DefaultSubView.as_view(), name='default'),
    path('subscription/', SubView.as_view(), name='sub')
]