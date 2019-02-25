from django.shortcuts import render

# Create your views here.
def index(request):
    theCode = request.GET.get('code')
    context = {'theCode': theCode}
    return render(request, 'theWeb/index.html', context)
