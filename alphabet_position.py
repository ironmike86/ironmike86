#codewar challenge successsssssssSSSSSS

def alphabet_position(text):
    solution = ''
    for i in range(0,len(text)):
        if 64 < ord(text[i]) < 91: #ASCII capital letters convert to string of numbers then add space between but not at the end
            solution += str(ord(text[i])-64)
            if i < len(text)-2:
                solution += ' '
            #this is creating an array of integers and is not the solution
            #solution.append(ord(text[i])-64)
        elif 96 < ord(text[i]) < 123: #ASCII capital letters convert to string of numbers then add space between but not at the end
            solution += str(ord(text[i])-96)
            if i < len(text)-2:
                solution += ' '
            #this is creating an array of integers and is not the solution
            #solution.append(ord(text[i])-96)
    return solution
