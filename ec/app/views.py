from django.shortcuts import render ,redirect
from .models import Product,Users,Cart
from django.http import JsonResponse
from django.http  import HttpResponse
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,"app/index.html")

def category(request,category):
    product= Product.objects.filter(category=category)
    tittle= Product.objects.filter(category=category).values('tittle')
    return render(request,"app/category.html",{'product':product, 'selected_type':category,'tittle':tittle }) 


def product_details(request ,id):
    product= Product.objects.get(id=id)
    return render(request,"app\productDetails.html", {'product':product})


def categoryTittle(request,tittle):
    product= Product.objects.filter(tittle=tittle)
    tittle= Product.objects.filter(category=product[0].category).values('tittle') ## get all the tittles of that category
    return render(request,"app/category.html",{'product':product, 'selected_type':category,'tittle':tittle })


def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')


def register(request):
    return render(request,'app/register.html')

def login(request):
    return render(request,'app/login.html')

def profile(request):
    return render(request,'app/profile.html')

def userRegister(request):
    if request.method =='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        address=request.POST['address']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        user=Users.objects.filter(Email=email)
        if user:
            message="User is already exist"
            return render(request, 'app/register.html',{'msg':message})
        else:
            if password==cpassword:
                newUser=Users.objects.create(firstName=fname,lastName=lname,Email=email,contact=contact,address=address,password=password)
                message="User register successfully !"
                return render(request,'app/login.html' ,{'msg':message})
            else:
                message="Please enter the correct password ."
                return render(request, 'app/register.html',{'msg':message})



def userLogin(request):
    if request.method == 'POST':
        email=request.POST['email']
        password= request.POST['password']
        user=Users.objects.get(Email=email)
        print(user)
        if user:
            if user.password==password:
                request.session['firstName']=user.firstName
                request.session['email']=user.Email
                return render(request, 'app/index.html')
                # redirect('userProfile')
                
            else:
                message= "UserName or Password are wrong ."
                return render(request,'app/login.html', {'msg':message})
        else:
            message= "User is incorrect ."
            return render(request, 'app/login.html',{'msg':message})    
            


def userProfile(request):
    userName=request.session.get('email')
    if userName:
        try:
            user= Users.objects.get(Email=userName)
            return render(request, 'app/profile.html',{'user':user})
        except Users.DoesNotExist:
            pass
    return redirect('userLogin')    


def editProfile(request, Email):
    user=Users.objects.get(Email=Email)
    return render(request, 'app/edit.html', {'user':user})

def updateProfile(request, Email):
    if request.method=='POST':
        user=Users.objects.get(Email=Email)
        user.firstName=request.POST['fname']
        user.lastName=request.POST['lname']
        user.address=request.POST['address']
        user.Email=request.POST['email']
        user.contact=request.POST['contact']
        user.save()
        return redirect('userProfile')


def cPassword(request):
    userName=request.session.get('email')
    if userName:
        try:
            user= Users.objects.get(Email=userName)
            return render(request, 'app/changePassword.html',{'user':user})
        except Users.DoesNotExist:
            pass
    return redirect('changePassword') 



def changePassword(request,Email):
    userName=request.session.get('email')
    print(userName)
    user=Users.objects.get(Email=userName)
    print(user)
    if request.method=='POST':
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        cpassword=request.POST['cpassword']
        if oldpassword==user.password:
            if newpassword==cpassword:
                user.password=newpassword
                user.save()
                message=" password change successfully !"
                return render(request, 'app/edone.html',{'msg':message})
            else:
                message=" password  and confirm password does not match ."
                return render(request, 'app/changePassword.html',{'msg':message})
        else:
            message="old password does not mathch"
            return render(request, 'app/changePassword.html',{'msg':message})    
        

def add_to_cart(request):
    userName=request.session.get('email')
    user=Users.objects.get(Email=userName)
    product_id=request.POST.get('prod_id')
    product=Product.objects.get(id=product_id)
    try:
        aval=Cart.objects.get(id=product_id)
    except:
        addcart=Cart.objects.create(user=user,product=product)    
    return redirect('show_cart')

def show_cart(request):
    userName=request.session.get('email')
    user=Users.objects.get(Email=userName)
    cart=Cart.objects.filter(user=user)

    amount=0
    for p in cart:
        value = p.quantity* p.product.discounted_price
        amount=amount + value

    totalamount = amount + 40    
    return render(request, 'app/addToCart.html',{'cart':cart ,'amount':amount,'totalamount':totalamount})

def pluscart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        # print(id)
        userName=request.session.get('email')
        user=Users.objects.get(Email=userName)
        print(user)
        c= Cart.objects.get(product=prod_id , user=user)
        print("the valueof c:",c)
        c.quantity+=1
        c.save()
        # userName=request.session.get('email')
        # user=Users.objects.get(Email=userName)
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40    

        # print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
           
        }
        return JsonResponse(data)


# def pluscart(request, id):
#     if request.method == 'GET':
#         print(id)
#         data={

#         }
#         return JsonResponse(data)



def minuscart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        userName=request.session.get('email')
        user=Users.objects.get(Email=userName)
        print(user)
        c= Cart.objects.get(product=prod_id)
        print(c)
        c.quantity-=1
        c.save()
        # userName=request.session.get('email')
        # user=Users.objects.get(Email=userName)
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40    

        print(prod_id)
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
           
        }
        return JsonResponse(data)
    

def removecart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        userName=request.session.get('email')
        user=Users.objects.get(Email=userName)
        print(user)
        c= Cart.objects.get(product=prod_id)
        print(c)
        c.delete()
        # userName=request.session.get('email')
        # user=Users.objects.get(Email=userName)
        cart=Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40    

        print(prod_id)
        data={
            
            'amount':amount,
            'totalamount':totalamount
           
        }
        return JsonResponse(data)
    

def checkOut(request):
    return render(request, 'app/checkout.html')