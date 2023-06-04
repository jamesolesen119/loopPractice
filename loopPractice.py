#In essence, use loops and lists to write every possible combination of
#the following characters: X, Q, Z, &, $, and K

#write the characters to a list
letters = ['X', 'Q', 'Z', '&', '$', 'K']

#We will use a quadruple nested for loop to determine all the 4 letter combinations

counter1 = 0
counter2 = 0

#display all combinations in ROWS of 10 

for i in range(len(letters)):
    for x in range(len(letters)):
        for y in range(len(letters)):
            for z in range(len(letters)):
                print(f"{letters[i]}{letters[x]}{letters[y]}{letters[z]} " , end ="")
                counter2 += 1
            
                if counter2 >= 10:
                    print()
                    counter2 = 0
        