#Task:Replacing the occurence of python in a sentence

#Taking input sentence that contains python
a=input("Please provide a sentence that contains string python :")
b=a.split(" ")
#replacing python with pythons
for i in range(len(b)):
    if(b[i]=="python"):
        b[i]="pythons"
#print result
print(b)
    
