=============================================================================
#Write your code below this line 👇
def paint_calc(height,width,cover):
    
    print(round((height*width)/5))
          
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

=Check the no is prime or not================================================
First *fork* your copy. Then copy-paste your code below this line 👇
Finally click "Run" to execute the tests
=============================================================================
def prime_checker(number):
    if n==2 or n==3:
        print('prime')
    if n==1:
        print("Not prime")
    if number%6==1 or 6-n%6==1:
        print("prime ")
    else:
        print("Not prime")
    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
=============================================================================
#message encoder and decoder 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from d8logo import logo
print(logo)
text = list(input("Type your message:\n").lower())
shift = int(input("Type the shift number:\n"))

#Don't change the code above 👆
def encrypt(text,shift):
        init=0
        for i in text:
            if text[init] in alphabet:
                text[init]=alphabet[int(alphabet.index(i))+shift]
                init+=1
        return text
def decrypt(eny,shift):
    init=0
    for i in text:
        if text[init] in alphabet:
          text[init]=alphabet[int(alphabet.index(i))-shift]
        init+=1
    return text
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt and 'no' to stop it :\n")
    if direction=='encode':
        text=encrypt(text,shift)
        print("Encoded text : ",''.join(text))        
    elif  direction=='decode':
        text=decrypt(text, shift)
        print("Decoded text : ",''.join(text))
    else:
        break       
#=============================================================================
