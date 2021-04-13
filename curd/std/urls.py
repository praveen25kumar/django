from django.urls import path

from . import views

urlpatterns=[

    path('c/',views.add,name='create'),
    path('d/<int:id>',views.delete,name='Delete'),
    path('u/<int:id>',views.update,name='Update'),


]