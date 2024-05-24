from django.shortcuts import render


def projects(request):
    context = {'projects': 'active'}
    return render(request, 'projects/projects.html', context)