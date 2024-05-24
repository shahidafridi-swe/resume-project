from django.shortcuts import render

def services(request):
    context = {'services': 'active'}
    return render(request, 'service/services.html', context)

