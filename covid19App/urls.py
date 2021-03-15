from django.urls import path
from .views import indexPage, loginPage, hospitalPage, registerPage, symptomPage, logoutPage

urlpatterns = [
    path('', loginPage, name='Login'),
    path('home/', indexPage, name='Index'),
    path('hospital/', hospitalPage, name='Hospital'),
    path('register/', registerPage, name='Register'),
    path('symtom/', symptomPage, name='Symptom'),
    path('logout/', logoutPage, name='Logout')
]
