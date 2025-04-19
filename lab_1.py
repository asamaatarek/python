#count Vowels 
text= input("Enter your text")
vowels=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in range(len(text)):
    if text[i] in vowels:
        count+=1
print("Vowels Number:" , count)
#Number of iti
nw_text=text.lower()
part="iti"
num=nw_text.count(part)
print("Number of iti is",num)
# Remove Vowels
new=""
for i in range(len(text)):
    if text[i] not in vowels:
        new+=text[i]
print("Text without Vowels:" , new)
#location of i
text=input()
letter="i"
loc =[]
for i in range(len(text)):
    if text[i] == letter:
        loc.append(i)

print("location of i " , loc)
#Mario Build
number=int(input("Enter your number:"))
for i in range (1,number+1):
    coulmn = " "*(number-i)
    print(coulmn+ "*"*i)

