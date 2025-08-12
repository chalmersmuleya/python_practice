def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    vowel_count = 0
    

    
    for letter in string: # go through each character in the string
        
        if letter in letters: # check if it's a letter by seeing if it's in the letters string
            
            if letter in vowels: # check if it's a vowel
                vowel_count += 1
    return vowel_count

  
    
def count_consonants(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    consonant_count = 0
    for letter in string:
        if letter not in vowels:
                consonant_count += 1
    return consonant_count



message = 'abc de'
print(count_vowels(message))
print(count_consonants(message))
