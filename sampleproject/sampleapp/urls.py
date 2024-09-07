from . import views
from django.urls import path

urlpatterns =[
    path('',views.index, name = 'index'),   #home is the name of the function defined in views 

    path('home/',views.home, name = 'home'), 

    path('add/',views.addition,name='addition'),#eth verthe aan we can only transfer from home page 
    
    path('results/',views.results,name='results'),
    
]