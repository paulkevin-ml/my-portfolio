def is_palindrome(text):
    text = text.lower().replace(" ","")
    left = 0
    right = len(text)-1
    while left < right:
       if text[left]!=text[right]:
           return False
       left +=1
       right -=1
    return True
print(is_palindrome("Was it a car or a cat i saw"))
    
    
