from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from backapp.models import vehicledb, userdb, admindb


# Create your views here.

# homepage of website

def homepage(req):
    return render(req,"index.html")

# adding vehicle information

def vehicleinfo(req):
    return render(req,"vehicle.html")

# saving vehicle information

def vehiclesave(req):
    if req.method == "POST":
        na = req.POST.get('vename')
        vt = req.POST.get('vetype')
        vm = req.POST.get('vemodel')
        vd = req.POST.get('vedescription')
        obj = vehicledb(vname=na,vtype=vt,vmodel=vm,vdescription=vd)
        obj.save()
        messages.success(req, "Vehicle Information saved...")

        return redirect(vehicleinfo)

# display vehicle information

def vehicledisplay(req):
    data=vehicledb.objects.all()
    return render(req,"displayvehicle.html",{'data':data})

# edit,update,delete of vehicle information

def editvehi(req,dataid):
    data=vehicledb.objects.get(id=dataid)
    print(data)
    return render(req,"editvehicle.html",{'data':data})

def updatevehicle(req,dataid):
    if req.method == "POST":
        vn=req.POST.get('vename')
        vt=req.POST.get('vetype')
        vm=req.POST.get('vemodel')
        vd=req.POST.get('vedescription')
        vehicledb.objects.filter(id=dataid).update(vname=vn,vtype=vt,vmodel=vm,vdescription=vd)
        messages.success(req, "Updated Successfully...!")

        return redirect(vehicledisplay)

def deletevehicle(req,dataid):
    data = vehicledb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Deleted Successfully...!")

    return redirect(vehicledisplay)


# super admin login

def supuserlogin(req):
    return render(req,"superlogin.html")


def superadminlogin(request):
    if request.method=="POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password'] = password_r
                messages.success(request, "login successfully")
                return redirect(homepage)

            else:
                messages.error(request, "Invalid User..!")

                return redirect(supuserlogin)
        else:
            return redirect(supuserlogin)


def superadminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully...!")

    return redirect(supuserlogin)

# admin index
def adminindex(req):
    return render(req,"indexadmin.html")

# display of vehicle information to admin

def displayvehicleadmin(req):
    data=vehicledb.objects.all()
    return render(req,"admindisplayvehicle.html",{'data':data})

# the admin can edit,update of the vehicle information

def editvehicleadmin(req,dataid):
    data = vehicledb.objects.get(id=dataid)
    print(data)
    return render(req,"adminvehicleedit.html",{'data':data})

def adminupdatevehicle(req,dataid):
    if req.method == "POST":
        vn=req.POST.get('vename')
        vt=req.POST.get('vetype')
        vm=req.POST.get('vemodel')
        vd=req.POST.get('vedescription')
        vehicledb.objects.filter(id=dataid).update(vname=vn,vtype=vt,vmodel=vm,vdescription=vd)
        messages.success(req, "Updated Successfully...!")

        return redirect(displayvehicleadmin)

# user login
def loginuser(req):
    return render(req,"userlogin.html")

def registeruser(req):
    return render(req,"userregister.html")

def indexuser(req):
    return render(req,"userindex.html")

def displayuser(req):
    data=vehicledb.objects.all()
    return render(req,"userdisplay.html",{'data':data})


def saveuser(request):
    if request.method == "POST":
        Us  = request.POST.get('username')
        pas = request.POST.get('password')
        Em  = request.POST.get('email')
        Cp  = request.POST.get("confirmpassword")
        if pas==Cp:
            obj = userdb(Username=Us,Password=pas,confirmpassword=Cp,Email=Em,)
        obj.save()
        messages.success(request, "Registered Successfully...!")
        return redirect(loginuser)

def userloginn(request):
    if request.method=='POST':
        Username_r=request.POST.get("username")
        Password_r=request.POST.get("password")

        if userdb.objects.filter(Username=Username_r,Password=Password_r).exists():
            request.session['username']=Username_r
            request.session['password']=Password_r
            messages.success(request, "Login Successfully...!")
            return redirect(displayuser)
        else:
            messages.error(request,"Invalid User..!")
            return render(request,'userlogin.html')

def userlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully...!")
    return redirect(loginuser)


# login of admin
def loginadmin(req):
    return render(req,"adminlogin.html")



def registeradmin(req):
    return render(req,"adminregister.html")



def saveadmin(request):
    if request.method == "POST":
        Us  = request.POST.get('usernamee')
        pas = request.POST.get('passwordd')
        Em  = request.POST.get('emaill')
        Cp  = request.POST.get("confirmpasswordd")
        if pas==Cp:
            obj = admindb(Username=Us,Password=pas,confirmpassword=Cp,Email=Em,)
        obj.save()
        messages.success(request, "Registered Successfully...!")

        return redirect(loginadmin)


def adminlogins(request):
    if request.method=='POST':
        Username_r=request.POST.get("username")
        Password_r=request.POST.get("password")

        if admindb.objects.filter(Username=Username_r,Password=Password_r).exists():
            request.session['username']=Username_r
            request.session['password']=Password_r
            messages.success(request,"login successfully")
            return redirect(displayvehicleadmin)
        else:
            messages.error(request,"invalid user")
    return render(request,'adminlogin.html')
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout successfully")
    return redirect(loginadmin)










