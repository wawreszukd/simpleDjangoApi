from django.shortcuts import render

def homePage(request):
    return render(request, 'homePage.html', context={'title':'home', 'authcheck': request.user.is_authenticated})