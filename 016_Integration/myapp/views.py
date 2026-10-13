from django.shortcuts import render
import razorpay
from django.http import HttpResponse,JsonResponse
 
 
# Create your views here.
def index(request):
    return render(request,"index.html")

def payment(request):
   
    amt = int(request.GET['amt'])
    client = razorpay.Client(auth=("rzp_test_TnM3wp19lgI5Tn", "lql1IJBPqnSYvEXPBFLWhGGe"))

    data = { "amount": amt*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    # Amount is in currency subunits.
    return JsonResponse(payment)