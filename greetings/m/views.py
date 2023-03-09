from django.shortcuts import render

# Create your views here.
#function based view

#class based view

from django.shortcuts import render

from django.views.generic import View

class GoodMoringView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"Morning.html")
    
class GooodAfternoonView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"Afternoon.html" )
    
class GoodNightView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"Night.html")
