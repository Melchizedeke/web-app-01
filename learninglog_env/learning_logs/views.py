from django.shortcuts import render,HttpResponse

def learning_logs_home(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')
