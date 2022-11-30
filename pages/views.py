from typing import ContextManager
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from listings.models import Listing
from realtors.models import Doctor
from contacts.models import Contacts


def index(request):
    listings= Listing.objects.order_by('-id').filter(is_published=True)[:3]

    context =    {
        'listings': listings

    }
    return render(request,'pages/index.html',context)

def about(request):
    doctors= Doctor.objects.order_by('-name')
    listings= Listing.objects.order_by('-id').filter(is_best=True)

    #MVP

    mvp_doctor=Doctor.objects.all().filter(is_mvp=True)

    context = {
        'doctors' : doctors,
        'mvp_doctor' : mvp_doctor,
        'listings': listings,
    }

    return render(request,'pages/about.html', context)


@login_required(login_url='login')
def bill(request,bill_id):


    data = Contacts.objects.get(id=bill_id)
    print(data)
    dict = {'data' : data}


    return render(request,'billing/bill.html',dict)