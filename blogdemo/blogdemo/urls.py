"""blogdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from  learn import views as  learn_views
from zqxt import views as zqxt_views

urlpatterns = [
    #url(r'^$',learn_views.index),
    url(r'^$',zqxt_views.index,name='home'),
    url(r'^add/$',zqxt_views.add,name='add'),
    # url(r'^add/(\d+)/(\d+)/$',zqxt_views.add2,name='add2'),
    url(r'^add/(\d+)/(\d+)/$',zqxt_views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/$', zqxt_views.add2, name='add2'),
    url(r'^admin/', admin.site.urls),
]
