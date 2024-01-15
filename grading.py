#Task:print letter grade based on class score

#Take input class score
a=float(input("Enter the score :"))
#grading criteria based on score
if(a>=90 and a<=100):
    print("the Grade is A")
elif(a>=80 and a<90):
    print("the Grade is B")
elif(a>=70 and a<80):
    print("the Grade is C")
elif(a>=60 and a<70):
    print("the Grade is D")
else:
    print("the Grade is F")
