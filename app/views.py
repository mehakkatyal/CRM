from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import userprofile,details,complaint,PSIONumber,TransactionAmount,DisputedAmount,Layer,Freeze,InwardDate,Update
from django.core.paginator import Paginator
def homepage(request):
 
        return render(request,'homepage.html')
def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("Username and password are not valid")
    
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        return render(request, 'login.html' ) 
def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/")
def createuser(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password=request.POST['password']
        email=request.POST['email']
        is_vendor=request.POST.get('is_vendor')

        if User.objects.filter(username=username).exists():
            return HttpResponse("Error:userrname already exists")
        
        user=User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()
        profile=userprofile.objects.create(
            user=user,
            is_vendor=is_vendor
        )
        profile.save()
        return HttpResponse("user is created sussfully")
    else:
        return render(request,'createuser.html')
@login_required
def add_details(request):
    if request.method == "POST":
        client_details = request.POST.get('client_details')
        account_balances = request.POST.get('account_balances')
        date = request.POST.get('date') 
        detail = details(
            user=request.user,
            client_details=client_details,
             account_balances=account_balances,
             date=date  
        )
        detail.save() 
        complaint_details_list = request.POST.getlist('complaint_details')
        complaint_objects = []
        for complaint_detail in complaint_details_list:
            complaint_obj = complaint.objects.create(
                detail=detail,  
                complaint_details=complaint_detail,
            
            )
            complaint_objects.append(complaint_obj)

      
        ps_io_numbers = request.POST.getlist('ps_io_number')  # Get multiple PS/IO numbers
        for i, ps_io in enumerate(ps_io_numbers):
            if i < len(complaint_objects):
                # Associate the PS/IO number with the corresponding complaint
                PSIONumber.objects.create(
                    complaint=complaint_objects[i],  # Link PS/IO number to the correct complaint
                    ps_io_number=ps_io
                )
            else:
                # Associate with the last complaint if there are more PS/IO numbers than complaints
                PSIONumber.objects.create(
                    complaint=complaint_objects[-1],
                    ps_io_number=ps_io
                )

        # Handle multiple transaction amounts
        transaction_amounts = request.POST.getlist('transaction_amount')
        for amount in transaction_amounts:
            TransactionAmount.objects.create(
                details=detail,  # Correct field name
                amount=amount
            )

        # Handle multiple disputed amounts
        disputed_amounts = request.POST.getlist('disputed_amount')
        for amount in disputed_amounts:
            DisputedAmount.objects.create(
                details=detail,  # Correct field name
                amount=amount
            )

        # Handle multiple freeze statuses
        freezes = request.POST.getlist('frezz')
        for freeze in freezes:
            Freeze.objects.create(
                details=detail,  # Correct field name
                status=freeze
            )

        # Handle multiple layers
        layers = request.POST.getlist('layer')
        for layer_value in layers:
            Layer.objects.create(
                details=detail,  # Correct field name
                layer=layer_value
            )

        # Handle multiple inward dates
        inward_dates = request.POST.getlist('inward_date')
        for inward_date in inward_dates:
            InwardDate.objects.create(
                details=detail,  # Correct field name
                inward_date=inward_date
            )

        # Handle multiple updates
        updates = request.POST.getlist('update')
        for update_text in updates:
            Update.objects.create(
                details=detail,  # Correct field name
                update_text=update_text
            )

        return HttpResponse("Your details have been added successfully.")

    return render(request, 'details.html')

@login_required
 
# def profile(request):




#     details_list = details.objects.filter(user=request.user)

#     paginator=Paginator(details_list,5)
#     page_number=request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     print(details_list)
#     return render(request, 'profile.html', {'page_obj':page_obj})
def profile(request):
    # Check if the current user is a vendor
    if request.user.userprofile.is_vendor:  # Assuming 'is_vendor' field in the profile model
        # If the user is a vendor, show all profiles
        details_list = details.objects.all()  
    else:
        # If the user is not a vendor, show only the current user's profile
        details_list = details.objects.filter(user=request.user)
    
    # Apply pagination
    paginator = Paginator(details_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    return render(request, 'profile.html', {'page_obj': page_obj})


def deldetail(request):
    det=details.objects.filter(user=request.user)
    det.delete()
    return HttpResponse("your details deleted sussfully")




