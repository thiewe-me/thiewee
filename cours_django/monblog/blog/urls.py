"""
    2eme urls.py
"""



from django.urls import path
from blog import views 

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('loml/', views.loml),
    path('articless/', views.articless),
    ]
