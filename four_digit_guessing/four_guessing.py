import random
first = random.randint(1,9)
trail = 0
second = random.randint(0,9)
while second == first:
        trail+=1
        second = random.randint(0,9)
        
third = random.randint(0,9)
while third == first or third == second:
        trail+=1
        third = random.randint(0,9)
        
forth = random.randint(0,9)
while forth == first or forth == second or forth == third:
        trail+=1
        forth = random.randint(0,9)
        
print("Boot success after ",trail," resets.")
print("Guess a 4-digit-number that each digit in this number is different from the others, and the first digit is not zero. \n You will get a result of xAyB for each of your guess, where x is the number of digit(s) that is in the right place, and y is the number of digit(s) that is in the 4-digit-number but in the wrong place. Good luck!")
count = 0
x = 0
while x != 4:
        x = 0
        y = 0
        guess = input("Enter your guess: ")
        gfirst = int(int(guess)/1000)
        gsecond = int((int(guess)-1000*gfirst)/100)
        gthird = int((int(guess)-(1000*gfirst+100*gsecond))/10)
        gforth = int(int(guess)-(1000*gfirst+100*gsecond+10*gthird))
        while gfirst == gsecond or gfirst == gthird or gfirst == gforth or gsecond == gthird or gsecond == gforth or gthird == gforth:
                print("InvalidArgument: digits cannot be the same.")
                guess = input("Enter your guess: ")
                gfirst = int(int(guess)/1000)
                gsecond = int((int(guess)-1000*gfirst)/100)
                gthird = int((int(guess)-(1000*gfirst+100*gsecond))/10)
                gforth = int(int(guess)-(1000*gfirst+100*gsecond+10*gthird))
        if gfirst == first:
                x+=1
        elif gfirst == second or gfirst == third or gfirst == forth:
                y+=1
        if gsecond == second:
                x+=1
        elif gsecond == first or gsecond == third or gsecond == forth:
                y+=1
        if gthird == third:
                x+=1
        elif gthird == first or gthird == second or gthird == forth:
                y+=1
        if gforth == forth:
                x+=1
        elif gforth == first or gforth == second or gforth == third:
                y+=1
        print(str(x),"A",str(y),"B")
        count+=1
        
print("That's it! You did it in ",count," trails, amigo.")
