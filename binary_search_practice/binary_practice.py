print("BINARY SEARCH PRACTICE")
import random
import math
state = "y"
print("Guess an integer between your selected boundry.")
while state == "y" or state == "Y":
        count = 0
        lrange = int(input("Choose the lower bound: "))
        rangel = int(input("Choose the higher bound: "))
        exp_count = int(math.log(rangel-lrange,2)+1)
        if exp_count >= 5:
                computer_choice = random.randint(lrange,rangel)
                user_choice = int(input("My guess is: "))        
                while user_choice != computer_choice:
                        if user_choice < computer_choice:
                                print("Too small.")
                                
                        else:
                                print("Too big.")
                        count+=1
                        user_choice = int(input("My guess is: "))
                count+=1
                
                if count == 1:
                        print("Nice shot! What a luck!")
                elif count < exp_count:
                        print("That's it! You did it in ",count," trails.")
                elif count == exp_count:
                        print("That's it! You did it in ",count," trails. However, it seems that your luck isn't that good.")
                else:
                        print("Your guess is finally correct after ",count," trails. It seems you need to improve your skill in binary serach or basic math skills. Visit https://en.wikipedia.org/wiki/Binary_search_algorithm for more information on binary search.")        
        else:
                print("The result will be inaccurate when the range is smaller than 16")
        state = input("You wanna try it again? [Y / N]")

exit
