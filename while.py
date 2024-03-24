
# first ask the user to enter the number and store it into variable
# using while loop check whether the number is digit if not ask again if yes cast it into float
# for this create function to check the string from user (could not find any other function)

def isfloat(str_ing):
    'The function accepts string parameter, and returns True if its rational numbers or False if not.'
    ch_eck = "0123456789."
    if str_ing[0] == '-':
        str_ing = str_ing[1::] # rewrite the string to allow negative input
    bool_r = True # bool_r keep what is have to be return
    if str_ing[0] == '.': # compare first char if it start with '.' If yes its not float
        bool_r = False
        return bool_r
    c_ount = 0 # count the amount of '.' if more than 2 - the string cannot be float
    for i in str_ing: # iterate over incoming string
        if i == '.':
            c_ount += 1
        for y in ch_eck: # iterate over sample chars
            if i == y:
                break
            if y == '.': # if counter 'y' comes to the end keep '.' - no matches found. 
                         # So some other char is present in the string.
                bool_r = False
        if c_ount > 1:
            bool_r = False
            break
    return bool_r

num = 0
total = 0
times = 0
average = 0
while num != -1:
    num_raw = input("Enter a number (-1 to quit):")
    while not isfloat(num_raw):
        num_raw = input("Enter a valid number (-1 to quit):")
    num = float(num_raw)
    total = total + num
    times = times + 1
    if num == -1:
        average = (total+1)/(times-1)
        break
print (f"Average of the numbers is {average}")