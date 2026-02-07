from django.contrib import admin
from django.urls import path
from content import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.category_videos, name='category_videos'),
    path('online-classes/', views.online_classes, name='online_classes'),
    path('enquiry/', views.enquiry_form, name='enquiry_form'),
     path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
]