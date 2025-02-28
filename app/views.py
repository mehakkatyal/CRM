from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import userprofile,details,complaint,PSIONumber

def homepage(request):
    # if request.method=="POST":
        # return HttpResponse("hello")
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
# def add_details(request):
#      if request.method=="GET":
#           return render(request,"details.html")
#      else:
#           client_details=request.POST.get('client_details')
#           complaint_details=request.POST.get('complaint_details')
#           ps_io_number=request.POST.get('ps_io_number')
#           account_balances=request.POST.get('account_balances')
#           transaction_amount=request.POST.get('transaction_amount')
#           disputed_amount=request.POST.get('disputed_amount')
#           frezz=request.POST.get('frezz')
#           layer=request.POST.get('layer')
#           date=request.POST.get('date')
#           update=request.POST.get('update')

#           detail=details.objects.create(
#                client_details=client_details,
#                complaint_details=complaint_details,
#                ps_io_number=ps_io_number,
#                account_balances=account_balances,
#                transaction_amount=transaction_amount,
#                disputed_amount=disputed_amount,
#                frezz=frezz,
#                layer=layer,
#                date=date,
#                update=update,
#                user=request.user
#           )
#           detail.save()
#           return HttpResponse("your details added sussfully")
# def add_details(request):
#     if request.method == "POST":
#         client_details = request.POST.get('client_details')
     
#         account_balances = request.POST.get('account_balances')
#         transaction_amount = request.POST.get('transaction_amount')
#         disputed_amount = request.POST.get('disputed_amount')
#         frezz = request.POST.get('frezz')
#         layer = request.POST.get('layer')
#         date = request.POST.get('date')
#         update = request.POST.get('update')


      
      
#         detail = details(
#                     user=request.user,
#                     client_details=client_details,
                 
#                     account_balances=account_balances,
#                     transaction_amount=transaction_amount,
#                     disputed_amount=disputed_amount,
#                     frezz=frezz,
#                     layer=layer,
#                     date=date,
#                     update=update
#                 )
#         detail.save()
#         complaint_details_list = request.POST.getlist('complaint_details')  # Assuming you pass multiple complaints

#         for complaint_detail in complaint_details_list:
#             complaint.objects.create(
#                 detail=detail,
#                 complaint_details=complaint_detail
#             )
#         ps_io_numbers = request.POST.getlist('ps_io_number')  # get multiple PS/IO numbers
#         for ps_io in ps_io_numbers:
#              PSIONumber.objects.create(
                
#                     ps_io_number=ps_io
                
#                 )
    

#         return HttpResponse("your details added ")  # Redirect to a success page or profile page
    
#     return render(request, 'details.html')
def add_details(request):
    if request.method == "POST":
        client_details = request.POST.get('client_details')
        account_balances = request.POST.get('account_balances')
        transaction_amount = request.POST.get('transaction_amount')
        disputed_amount = request.POST.get('disputed_amount')
        frezz = request.POST.get('frezz')
        layer = request.POST.get('layer')
        date = request.POST.get('date')
        update = request.POST.get('update')

        # Create the detail object first
        detail = details(
            user=request.user,
            client_details=client_details,
            account_balances=account_balances,
            transaction_amount=transaction_amount,
            disputed_amount=disputed_amount,
            frezz=frezz,
            layer=layer,
            date=date,
            update=update
        )
        detail.save()

        # Create complaints and link them to the 'detail' object
        complaint_details_list = request.POST.getlist('complaint_details')
        complaint_objects = []

        for complaint_detail in complaint_details_list:
            complaint_obj = complaint.objects.create(
                detail=detail,  # Link complaint to the detail object
                complaint_details=complaint_detail
            )
            complaint_objects.append(complaint_obj)

        # Create PSIONumber objects and associate each one with a complaint
        ps_io_numbers = request.POST.getlist('ps_io_number')  # Get multiple PS/IO numbers
        for i, ps_io in enumerate(ps_io_numbers):
            if i < len(complaint_objects):
                # Associate the PSIONumber with the corresponding complaint
                PSIONumber.objects.create(
                    complaint=complaint_objects[i],  # Link PSIONumber to the correct complaint
                    ps_io_number=ps_io
                )
            else:
                # Handle case if there are more PS/IO numbers than complaints (ensure correct association)
                PSIONumber.objects.create(
                    complaint=complaint_objects[-1],  # Associate with the last complaint if no match
                    ps_io_number=ps_io
                )

        return HttpResponse("Your details have been added successfully.")  # Or redirect to the profile or success page
    
    return render(request, 'details.html')

@login_required
# def profile(request):
#     pro=details.objects.filter(user=request.user)
#     return render(request,'profile.html',{'pro':pro})  
# def profile(request):
#     details_list = details.objects.filter(user=request.user)
#     return render(request, 'profile.html', {'details_list': details_list})   
def profile(request):
    # Fetch the details associated with the logged-in user
    details_list = details.objects.filter(user=request.user)
    print(details_list)
    
    # Render the profile template with the details_list
    return render(request, 'profile.html', {'details_list': details_list})
def deldetail(request):
    det=details.objects.filter(user=request.user)
    det.delete()
    return HttpResponse("your details deleted sussfully")




