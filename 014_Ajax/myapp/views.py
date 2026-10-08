from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def test(request):
    q = request.GET.get("q")
    return HttpResponse(f"Hello {q}")

def search(request):
    q = request.GET.get("q")
    
    # resp = ""
    # if q=='sport':
    #     resp+="<ul><li>Ball</li><li>Bat</li><li>Cap</li></ul>"
    # elif q=='electric':
    #         resp+="<ul><li>Fan</li><li>Tv</li><li>Laptop</li></ul>"
    # else:
    #     resp+="No product found"
    
    resp="<ul>"
    products = product.objects.filter(name__startswith=q)
    for pro in products:
        resp+=f"<li>{pro.name}</li>"
    resp+="</ul>"
    return HttpResponse(resp)


def countries(request):
    countries = Country.objects.all()
    return JsonResponse({"data":list(countries.values())})


def states(request):
    cid  =request.GET.get("cid")
    states = State.objects.filter(country_id=cid)
    return JsonResponse({"data":list(states.values())})


def cities(request):
    sid  =request.GET.get("sid")
    states = City.objects.filter(state_id=sid)
    return JsonResponse({"data":list(states.values())})
    