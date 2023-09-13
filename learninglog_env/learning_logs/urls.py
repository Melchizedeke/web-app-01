from django.urls import path
from . import views
urlpatterns = [
    # Home Page
    path("", views.learning_logs_home, name="learning_logs_home"),
    
    # Show all Topics
    path("topics/", views.topics, name='topics'),
]