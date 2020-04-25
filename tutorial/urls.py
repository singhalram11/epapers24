from django.urls import path
from . import views
urlpatterns = [
    path('programmingsolutions',views.tutorial, name='programmingsolutions'),
    path('newpage', views.newpage, name='newpage'),

]
