from django.shortcuts import render

# from django.http import HttpResponse
# def homePageView(request):
#     return HttpResponse("My New App!")

def homePageView(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')
