from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('done/<id>', views.Done,name='Done'),
    path('notdone/<id>', views.NotDone,name='NotDone'),
    path('delete/<id>', views.delete,name='delete'),
]