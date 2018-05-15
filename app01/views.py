from django.shortcuts import render,HttpResponse
from app01 import  models
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,'index.html')


def ajax1(request):
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    return HttpResponse('okok')

def upload(request):
    return render(request,'upload.html')

def uploaded(request):
    import os,json,uuid
    ret = {'status':True,'data':None}
    obj = request.FILES.get('k3')
    file_path = os.path.join('static',str(uuid.uuid4()) + obj.name)
    with open(file_path,'wb') as f:
        for line in obj.chunks():
            f.write(line)
    ret['data'] = file_path
    return HttpResponse(json.dumps(ret))


def jsonp(request):
    return render(request,'jsonp.html')

def jsonpcommit(request):
    return HttpResponse('local 我要上小云')

def bxslider(request):
    return render(request,'bxsliderTest.html')

def zan(request):
    return render(request,'zan.html')

def article(request,*args,**kwargs):
    url = reverse('article',kwargs=kwargs)
    print('url',url)

    condition = {}
    for k,v in kwargs.items():
        kwargs[k] = int(v)
        if v == '0':
            pass
        else:
            condition[k] = v

    article_type_list = models.ArticleType.objects.all()
    category_list = models.Category.objects.all()
    result = models.Article.objects.filter(**condition)
    return render(
        request,
        'article.html',
        {'result':result,
         'article_type_list':article_type_list,
         'category_list':category_list,
          'arg_dict':kwargs}
    )

def picwall(request):
    return render(request,'picwall.html')

def getdata(request):
    from django.http import JsonResponse
    nid = request.GET.get('nid')
    ret = {'status':True,'data':None}
    obj_list = list(models.FileTest.objects.filter(id__gt=nid).values('id','src','title'))
    ret['data'] = obj_list
    return JsonResponse(ret)

