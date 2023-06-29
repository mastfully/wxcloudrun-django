from django.urls import path
from . import views

urlpatterns = [
    path('camps', views.CampsView.as_view()),
    path('set', views.SetTbView.as_view()),
    path('enroll', views.SignUpView.as_view())
]