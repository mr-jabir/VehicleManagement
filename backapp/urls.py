from django.urls import path
from backapp import views

urlpatterns=[
path('homepage/',views.homepage,name="homepage"),
path('vehicleinfo/',views.vehicleinfo,name="vehicleinfo"),
path('vehiclesave/',views.vehiclesave,name="vehiclesave"),
path('vehicledisplay/',views.vehicledisplay,name="vehicledisplay"),
path('editvehi/<int:dataid>/',views.editvehi,name="editvehi"),
path('updatevehicle/<int:dataid>/',views.updatevehicle,name="updatevehicle"),
path('deletevehicle/<int:dataid>/',views.deletevehicle,name="deletevehicle"),
path('',views.supuserlogin,name="supuserlogin"),
path('superadminlogin/',views.superadminlogin,name="superadminlogin"),
path('superadminlogout/',views.superadminlogout,name="superadminlogout"),
path('loginadmin/',views.loginadmin,name="loginadmin"),
path('displayvehicleadmin/',views.displayvehicleadmin,name="displayvehicleadmin"),
path('editvehicleadmin/<int:dataid>/',views.editvehicleadmin,name="editvehicleadmin"),
path('adminupdatevehicle/<int:dataid>/',views.adminupdatevehicle,name="adminupdatevehicle"),
path('adminindex/',views.adminindex,name="adminindex"),
path('loginuser/',views.loginuser,name="loginuser"),
path('indexuser/',views.indexuser,name="indexuser"),
path('displayuser/',views.displayuser,name="displayuser"),
path('registeruser/',views.registeruser,name="registeruser"),
path('saveuser/',views.saveuser,name="saveuser"),
path('userloginn/',views.userloginn,name="userloginn"),
path('userlogout/',views.userlogout,name="userlogout"),
path('loginadmin/',views.loginadmin,name="loginadmin"),
path('registeradmin/',views.registeradmin,name="registeradmin"),
path('saveadmin/',views.saveadmin,name="saveadmin"),
path('adminlogins/',views.adminlogins,name="adminlogins"),
path('adminlogout/',views.adminlogout,name="adminlogout"),



]