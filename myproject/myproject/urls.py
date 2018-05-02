
from django.conf.urls import include, url
from django.contrib import admin
from cms import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.inicio),
    url(r'^login','django.contrib.auth.views.login'),
    url(r'^accounts/profile/$' , views.user_login),
    url(r'^logout',views.user_logout),
    url(r'^pagina/(\d+)',views.mostrar),
]
