import random

points= 300



play_again ="y"


while (points>0) and (play_again == 'y'):

    cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    random_num = random.choice(cards)

    remove_number = cards.index(random_num)

    cards.pop(remove_number)

    next_random_num = random.choice(cards)

    print(f"The card is: {random_num}")

    print()
    
    guess_h_or_l = input("Higher or lower? [h/l] :").lower()

    print()
    
    print(f"Next card was: {next_random_num}")

    if (random_num < next_random_num) and (guess_h_or_l == 'h'):

        points+=100
        
    elif (random_num > next_random_num) and (guess_h_or_l == 'l'):
        points+=100
    
    else:
        points-=75

    print (f"Your score is: {points}")

    print()

    play_again =input("Play again? [y/n] ")

print()
print("THANKS FOR PLAYING")



    

