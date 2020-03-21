def intToRoman(s):
    num = 0
    counter = 0
    for char in s:
        if(char == 'L'):
            counter+=1
        else:
            counter-=1
        if(counter == 0):
            num += 1
    return num
    
print(intToRoman('LSLS'))