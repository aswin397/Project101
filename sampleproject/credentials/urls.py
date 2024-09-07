from . import views
from django.urls import path

urlpatterns =[

    path('register',views.register, name = 'register'),   #home is the name of the function defined in views 
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
    
]