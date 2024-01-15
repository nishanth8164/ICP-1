#Task:Take list of characters from console and delete atleast 2 strings and reverse the string

#Input the string python as list
input_string=input("Please provide the string "'Python'" ")
string_list=list(input_string)
#delete atleast 2 characters
index=0
for i in range(2):   
    del string_list[index]
#reverse the resultant string   
string_list.reverse()
#print the output
print(''.join(string_list))



#Task:Perform arithmetic operations on two numbers
print("Arthmetic Operations Section Begins. Please provide any two numbers")
#Take input from user
a=int(input())
b=int(input())
#perform arithmetic operations and print the result
c=a+b
print("addition of two numbers",a,"and",b," is :",c)

c=a-b
print("subtraction of two numbers",a,"and",b," is :",c)

c=a*b
print("multiplication of two numbers",a,"and",b," is :",c)

c=a%b
print("modulo division of two numbers",a,"and",b," is :",c)




