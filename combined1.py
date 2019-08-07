class combined:

    def fibonacci(self):
        fibnumber=int(input("enter the no for which fibonaaci series required"))
        a=0
        second=1
        first=0
        while(a<fibnumber):
            if(a<=1):
                d=a
                print(d)
            else:
                d=first+second
                first=second
                second=d
            print("fibnacci series as follows:",d)
            a=a+1
    l=[]
    def listed(self):
        b=int(input("enter the total of no of elements to be entered in list"))
        for i in range(1,b):
            a=int(input("enter the no:"))
            self.l.append(a)
        print(self.l)
    def Target(self):
        b=int(input("enter the target no:"))
        for i in range(0,len(self.l)-1):
            if((self.l[i]+self.l[i+1])==b):
                print("first value is",self.l[i],"second values is :",self.l[i+1])

    p = []
    def Length(self):
        
        a=int(input("enter the no of lenth values to be entered in "))
        for i in range(1,a):
            b=int(input("enter the values"))
            self.p.append(b)
        print(self.p)

    k = []
    def Width(self):
        
        c=int(input("enter the no of width values to be entered in "))
        for j in range(1,c):
            e=int(input("enter the values"))
            self.k.append(e)
        print(self.k)
        
    def Area(self):
        for s in range(0,len(self.p)):
            print("Area of rectangle:",self.p[s]*self.k[s])
            
    def fac(self):
        y=int(input("enter the no for whom factorial is required"))
        fact = 1
       
        for i in range(1,y+1):
            fact*=i
            print("factorial of no is:",fact)
              
    

x=combined()
print("press 1 for area of rectangle")
print("press 2 for fibonacci series")
print("press 3 for target number" )
print("press 4 for factorial of a number")
h=int(input("Now select a option:"))
if(h==1):
    x.Length()
    x.Width()
    x.Area()
elif(h==2):
    x.fibonacci()
elif(h==3):
    x.listed()
    x.Target()
elif(h==4):
    x.fac()
else:
    print("enter a valid option")
            
		
