from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contacts
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listings = request.POST['listings']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        doctor = request.POST['doctor']
        age = request.POST['age']

        contact = Contacts(listings = listings, listing_id = listing_id, name = name, email = email, phone = phone , message= message, age=age, user_id = user_id,doctor=doctor)

        contact.save()
        
        messages.success(request, "Your appointment has been saved and you can check it's status in My Appointments witnhin 1 hour.")

    return redirect('/listings/'+listing_id)


@login_required(login_url='login')
def appointment(request):
    
    user = request.user

    print(user.id)

    appointments = Contacts.objects.all().filter(user_id = user.id)

    context = {'appointments' : appointments,}


    return render(request, 'contacts/appointment.html',context)