from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from .models import Listing
from realtors.models import Doctor

def index(request):
    listings=Listing.objects.all()

    paginator= Paginator(listings, 1)

    page = request.GET.get('page')

    paged_listings = paginator.get_page(page)

    context= {
        'listings' : listings
    }
    return render(request, 'listings/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    best_hosp=Listing.objects.all().filter(is_best=True)
    
    doctors = []

    doc = Doctor.objects.all()

    for d in doc:
        for h in d.hospital.all():
            if(h.id == listing_id):
                doctors.append(d)

    print(doctors)
   

    contex = {
        'listing': listing,
        'best_hosp' : best_hosp,
        'doctors' : doctors,
    }

    return render(request, 'listings/listing.html', contex)
    
def search(request):
    return render(request, 'listings/search.html')