"""
URL configuration for electronic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from electro import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name='home'),
    path('contact',views.ContactView.as_view(),name='contact'),
    path('review',views.ReviewView.as_view(),name='review'),
    path('allreview',views.AllReviewView.as_view(),name='allreview'),
    path('subscribe',views.SubscribeView.as_view(),name='subscribe'),

    path('register',views.RegisterVIEW.as_view(),name='register'),
    path('userlogin',views.userLoginVIEW.as_view(),name='userlogin'),
    
    path('appointment',views.AppointmentVIEW.as_view(),name='appointment'),
    path('view_appointment/<int:id>',views.View_AppointmentVIEW.as_view(),name='view_appointment'),
    path('delete_appointment/<int:id>',views.Delete_AppointmentVIEW.as_view(),name='delete_appointment'),
        path('logout',views.userlogout,name='logout'),









    
    
    

      
]
