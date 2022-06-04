

marks=int(input("Enter your marks : "))

if marks> 80:
    print("Your grade is A")
elif marks>60 & marks<=80:
    print("Your grade is B")
elif marks>50 & marks<=60:
    print("Your grade is C")
elif marks>45 & marks<=50:
    print("Your grade is D")
elif marks>25 & marks<=45:
    print("Your grade is E")
else:
    print("Your grade is F")



year=int(input("enter the year : "))

if year%4==0:
    print("entered year is a leap year")
elif year%100==0 & year%400==0:
    print("entered year is a leap year")
else:
    print("entered year is not a leap year")





import random
i=0
while i<10:
    a=random.randint(0,10)
    b=random.randint(0,10)
    
    print("Solve {}*{}=".format(a,b))
    ans=int(input("Enter your answer:",))
    
    if ans==a*b:
        print("Right")
    else:
        print("Wrong. The answer is {}".format(a*b))
    i+=1
    




for candies in range(200):
    if candies % 5 == 2:
        if candies % 6 == 3:
            if candies % 7 == 2:
                print(candies,'candies are in the bowl!')

