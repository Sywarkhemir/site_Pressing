from django.urls import path,include
from . import views
app_name = 'pressing'
urlpatterns = [
    path('',views.home,name="home"),
    path('logout/',views.logoutUser,name="logout"),
    path('contact/',views.contact,name="contact"),
    path('Feedbacks/',views.notif,name="notif"),
    path('Case-Of-Linge/<str:ch>',views.clothes,name="clothes"),
]
