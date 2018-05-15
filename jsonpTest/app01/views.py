from django.shortcuts import render,HttpResponse

# Create your views here.
# def index(request):
#     print(request.GET)
#     name = request.GET.get('callback')
#     print(name)
#     return HttpResponse("%s('remote 我要上小云')" % name)

def index(request):
    obj = HttpResponse('我要强上小云')
    obj['Access-Control-Allow-Origin'] = '*'
    return obj