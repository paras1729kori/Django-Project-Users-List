from django.conf.urls import url
from apptwo import views

urlpatterns = [
    url('users/', views.users, name='users')
]
