# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    str1 = input ("1word:")
str2 = input ("2word")
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)
 
if sorted_str1 == sorted_str2:
     print("True")
else:
         print("False")

    
      

