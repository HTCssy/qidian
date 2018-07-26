
from django.conf.urls import url

from apps.user import views

urlpatterns = [
    url(r'login/', views.login),
    url(r'register/', views.register),
    url(r'error/', views.error),
    url(r'get_session/', views.get_session),
    url(r'login_out/', views.login_out),
]
