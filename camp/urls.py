from django.urls import path
from . import views

urlpatterns = [
    path('camps', views.CampsView.as_view())
]