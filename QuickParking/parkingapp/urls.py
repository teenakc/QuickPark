from django.contrib import admin
from django.urls import path
from parkingapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="home"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('signup/',views.signup, name="signup"),
    path('login/',views.user_login, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('signup/',views.signup,name="signup")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)