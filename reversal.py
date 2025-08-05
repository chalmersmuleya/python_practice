def reversal(string):
    rev = string[::-1]
    if string == rev:
        return True
    else:
        return False

print(reversal("hannah"))