from django.shortcuts import render
from django.views.generic import View
from django import forms

class Operationform(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()


class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class Registrationform(forms.Form):
    firstname=forms.CharField()
    secondname=forms.CharField()
    email=forms.CharField()
    password=forms.CharField()


# Create your views here.

class AdditionView(View):
    def get(self,request,*args,**kwargs):
        form=Operationform()

        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):

        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))

        res=n1+n2
        print(res)

        return render(request,"add.html",{"result":res})
    
# class AdditionView(View):
#     def get(self,request,*args,**kwargs):

#         return render(request,"add.html")
    
#     def post(self,request,*args,**kwargs):

#         n1=int(request.POST.get("num1"))
#         n2=int(request.POST.get("num2"))

#         res=n1+n2
#         print(res)

#         return render(request,"add.html",{"result":res})


class SubtractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")
    
    def post(self,request,*args,**Kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1-n2
        print(res)
        return render(request,"sub.html")
    


class Multiplication(View):
    def get(self,request,*args,**kwargs):

        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):

        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))

        res=n1*n2
        print(res)

        return render(request,"mul.html",{"result":res})
    

class CubeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"cube.html")
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))
        res=n**3
        return render(request,"cube.html",{"result":res})
    

class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"fact.html")
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))

        fact=1
        for i in range(1,(n+1)):
             fact=fact*i
        return render(request,"fact.html",{"result":fact})






class Armstrong(View):
  
    def get(self,request,*args,**kwargs):
        return render(request,"armstrong.html")
    
    def post(self,request,*args,**kwargs):
        num=int(request.POST.get("num"))
        ln = len(num)
        sum = 0
        num=int(num)
        original=num
        while (num!=0):
            digit = num%10
            sum=sum+(digit**ln)
            digit = num//10
        result=sum==original
        return render (request,"armstrong.html",{"res":result}) 
    

class Prime(View):
  
    def get(self,request,*args,**kwargs):
        return render(request,"prime.html")
    
    def post(self,request,*args,**kwargs):
        num=int(request.POST.get("num"))

        flag=0
        for i in range (2,num):
            if num%i==0:
                flag=1
                break
        result="number is not prime" if flag==1 else "number is prime"
        
        return render(request,"prime.html",{"result":result})



# class Palindrome(View):
  
#     def get(self,request,*args,**kwargs):
#         return render(request,"palindrome.html")
    
#     def post(self,request,*args,**kwargs):
#         num=int(request.POST.get("num"))






class Even(View):
    def get(self,request,*args,**kwargs):

        return render(request,"even.html")
    def post(self,request,*args,**kwargs):
        l1=int(request.POST.get("limit1"))
        l2=int(request.POST.get("limit2"))

        even=[num for num in range(l1,l2) if num%2==0]

        # evens=[]
        # for num in range(l1,l2):
        #     if num%2==0:
        #         evens.append(num)
        return render(request,"even.html",{"result":even})
    


class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html")
    

class Health(View):
  
    def get(self,request,*args,**kwargs):
        return render(request,"health.html")
    
    def post(self,request,*args,**kwargs):
        tummy_size=request.POST.get("tummysize")
        buttock_size=request.POST.get("buttocksize")
        gender=request.POST.get("gender")
        bmi=int(tummy_size)/int(buttock_size)
        bmi=round(bmi,2)
        context={"gender":"","risk":"","shape":""}

        if gender=="male":
            if bmi <= .95:
                context["gender"]="male"
                context["risk"]="low"
                context["shape"]="pear"
            elif bmi >= .95 and bmi <= 1:
                context["gender"]="male"
                context["risk"]="moderate"
                context["shape"]="avocado"
            elif bmi > 1:
                context["gender"]="male"
                context["risk"]="high"
                context["shape"]="apple"
        else:
            if bmi <= .80:
                context["gender"]="female"
                context["risk"]="low"
                context["shape"]="pear"
            elif bmi >= .81 and bmi <= .85:
                context["gender"]="female"
                context["risk"]="moderate"
                context["shape"]="avocado"
            elif bmi >= .85:
                context["gender"]="female"
                context["risk"]="high"
                context["shape"]="apple"


        return render(request,"health.html",context)

class Temperature(View):
    def get(self,request,*args,**kwargs):
        return render (request,"temp.html")
    def post(self,request,*args,**kwargs):
        te=int(request.POST.get("num"))
        t=(te*(9/5))+32
        return render(request,"temp.html",{"result":t})

        

    


class Exponentview(View):
    def get(self,request,*args,**kwargs):
        form=Operationform()
        return render(request,"exponent.html",{"form":form})
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        exponent=n1**n2
        return render(request,"exponent.html")
    

class Loginview(View):
    def get(self,request,*args,**kwargs):
        form=Loginform()
        return render(request,"login.html",{"form":form})
    
class Registrationview(View):
    def get(self,request,*args,**kwargs):
        form=Registrationform()
        return render(request,"registration.html",{"form":form})
    

    

    





        

    


    



        


        
