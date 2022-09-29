"""site_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf (URL 권한 위임)
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lotto import views

# 메인 URL은 생략되서 적는다
urlpatterns = [
    path('admin/', admin.site.urls), # 주소는 http://127.0.0.1:8000/adimin
    # path('', views.index), # views. 파일의 index에게 넘겨주라는 의미, 주소는 http://127.0.0.1:8000/
    path('hello/', views.hello, name='hello_main'), # 주소는 http://127.0.0.1:8000/hello
    # 참고 : 실제론 URL패턴, 함수이름, name(별명)이 동일한 이름을 써준다.
    path('lotto/', views.index, name='index'),
    path('lotto/new', views.post, name = "new_lotto"),
    # lottokey는 detail() 함수의 parameter name 
    path('lotto/<int:lottokey>/detail', views.detail, name='detail')
]

