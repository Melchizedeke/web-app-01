from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home Page
    path("", views.learning_logs_home, name="learning_logs"),
    
    # Show all Topics
    path("topics/", views.topics, name='topics'),
]