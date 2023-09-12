from django.urls import path
from . import views
urlpatterns = [
    path("", views.learning_logs_home, name="learning_logs"),
]