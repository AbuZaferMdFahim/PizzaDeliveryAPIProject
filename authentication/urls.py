from django.urls import path
from . import views

urlpatterns=[
     path('',views.HelloAuthView.as_view(),name="helloAuth"),
     path('signup/',views.UserCrateView.as_view(),name="signUp"),
]