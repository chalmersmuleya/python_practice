#pascal case
def solve(s):
    words = s.split(" ") #split the words in string using space
    capitilized_words = (word.capitalize() for word in words) #capitilize every first letter of each word
    return " ".join(capitilized_words) #rejoin the capitalized words into one string using space as a separator

print(solve("this is the best day"))