#Sort
elemnts = []
print("enter 5 string elements:")
while True:
    if len(elemnts) == 5:
        break
    ele = input("element:")
    if ele.strip().isalpha():
        elemnts.append(ele)
    else:
        print("Only strings")
 
def asc_sort(l):
    for i in range(len(l)):
        for j in range(len(l)- i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    print("ascending",l)

def desc_sort(l):
    for i in range(len(l)):
        for j in range(len(l)- i - 1):
            if l[j] < l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    print("descending",l)

print("list:", elemnts)
asc_sort(elemnts)
desc_sort(elemnts)

# Multiplication 
n = int(input("enter number:"))
multiply=[]
for i in range(1, n + 1):
    number=n*i
    multiply.append(number)
    if number==n*n:
        break
print(f"Multiply list for {n} : ",multiply)

# length , start
length = int(input("enter length of array: "))
start = int(input("enter start point: "))
arr=[]
for i in range(length):
    arr.append(start+i)
print("the List is: ",arr)

num=int(input("enter number: "))
if num%5==0 and num%3==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("buzz")
else:
    print("number is not divisable by 3 or 5")

# reverse
x=input("Enter your string ")
reverse_x="".join(reversed(x))
print(reverse_x)

# str
import re
name_user=input("enter your name :")
if name_user and name_user.isdigit():
    print("enter name not empty or number..")
elif not name_user.isalpha():
    print("enter only string letters")
else:
    mail=input("enter your email :")
    # check email
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', mail):
        print("not valid email addressing")
    else:
        dic={"name":name_user,"e-mail":mail}
        print("your data : " ,dic)
  