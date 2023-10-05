from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="home"),
    path('contact', contact, name="contact"),
    path('login', loginUser, name="login"),
    path('logout', logoutUser, name="logout"),
    # path('register', registerUser, name="register"),

]