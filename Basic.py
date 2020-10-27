#Convert List to integer. Syntax: convertInt(list). Does not permently convert
def convertInt(list): 
        s = [str(i) for i in list] 
        res = int("".join(s))
        return(res)

#Convert List to string. Syntax: convertStr(list). Does not permently convert
def convertStr(list):
    s = [str(i) for i in list]
    res = str("".join(s))
    return(res)

loop = 1
while loop == 1:
    command = input(">>>")
    loop = 0
while loop == 0:
    #split at "+"
    x = command.rsplit("+")

    #find the length of the list and set middle_index to half of that
    length = len(x)
    middle_index = length//2

    #set first_half and second_half
    first_half = x[:middle_index]
    second_half = x[middle_index:]
    
    #set answers
    answerInt = convertInt(first_half) + convertInt(second_half)
    answerStr = convertStr(first_half) + convertStr(second_half)
    print(answerInt); print(answerStr)
    loop = 1