"""#Longest SubString
def long_substring(s):
    last_index = s[0]
    anthr = last_index
    longest = last_index
    for i in range(1,len(s)):
        if s[i] >= last_index:
            anthr += s[i]    
        else:
            anthr = s[i]  
        if len(anthr) > len(longest):
            longest = anthr
        last_index = s[i]
    return(longest)
text=input("Enter your string: ")
print(long_substring(text))
"""
#Done
"""
def num_until_done():
    count=0
    total =0
    print("Enter numbers until word done...")
    while True:
        num=input("Enter your number: ")
        if num.isdigit():
            num=int(num)
            count+=1
            total+=num
            continue
        elif num.lower()=="done":
            break
        else:
            print("..........only numbers......")
    if count > 0:
        print(f"count of numbers: {count}\ntotal of numbers: {total}\nAverage of numbers: {total/count}")
    else:
        print("count is 0")
num_until_done()"""
#HangMan
import random
def hangman(l):
    word = random.choice(l)
    print("Guess the word..")
    output = ['_' for _ in word]
    try_num=7
    letterGuess=""
    while try_num >0:
        print(' '.join(output))
        guess = input(f"\nEnter your letter guess:" ).lower()
        if len(guess)!=1:
            print("Enter one letter")
        elif guess in letterGuess:
            print("you already guessed this letter ")
        elif guess.isalpha() and guess in word:
            print("Right Guess !!")
            letterGuess += guess
            for i in range(len(word)):
                if word[i] == guess:
                    output[i] = guess   
        else: 
            try_num-=1
            print(f"wrong guess...you have cahnce:{try_num}")
        if "_" not in output:
            print(' '.join(output),"\nYou Won!!!!!!!!")
            break
    else:
        print("Lost!!!!!!!")

our_list=["ahmed","mohamed"]
hangman(our_list)