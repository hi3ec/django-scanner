from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    context = {
        'username': 'amir',
        'age':22,
        'job':'it',
    }
    return render(request, 'blog/home.html', context)

