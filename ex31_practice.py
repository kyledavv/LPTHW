import random
#Basic explanation of the rules
print("Here is the sport of tennis explained in a game.")
print("""First, you spin a racquet to see who serves first.
The winner of the racquet spin gets to choose whether to serve or return,
or which side of the court they would like to start on.""")
print("Which type of racquet will you be spinning? The options are Wilson, Head, Babolat, Yonex, or Other.")

#list of possible serves/returns to hit for each point
return_options = ['crosscourt', 'down the line', 'to the middle']
serve_options_deuce = ['slice out wide', 'slice in body', 'flat down the T']
serve_options_ad = ['slice down the T', 'flat in body', 'flat out wide']

#first input to see which racquet brand gets chosen- then branches to wilson spin or up/down spin
racquet = input("Racquet Brand > ").lower()

#wilson spin if stmnt. from input above.
if racquet == "wilson":
#sets the input of m or w for a wilson racquet spin. .lower() normalizes it to lower case.
    spin_wilson = input("M or W > ").lower()
#spin_option_wilson compares the input to m or w, then wilson_spin sets the random function for the spin toss
    spin_option_wilson = ['m', 'w']
    wilson_spin = random.choice(spin_option_wilson)


#if inside if: compares input of m or w to result of random spin. if win, sets choice to serve/receive. if lose, choice of side to go to
    if spin_wilson == wilson_spin:
        print("Congratulations, you won the toss. You get to choose whether to serve or receive.")

        serve_receive = input("Serve or Receive > ").lower()

        print(f"You chose to {serve_receive}. Here are the balls.")

        print("Below is a list of the possible serves to hit.")

        for serving_deuce in serve_options_deuce:
            print(f"> {serving_deuce}")
        serve_love_all = input("Which serve from above will you hit? ").lower()
        print(f"You hit a {serve_love_all} serve.")
        print("It was an ACE! You are winning 15-0.")

        for serving_ad in serve_options_ad:
            print(f"> {serving_ad}")
        serve_fifteen_love = input("The score is 15-0. Which serve from above will you hit next?")
        print(f"You hit a {serve_fifteen_love} serve.")
        print(f"Your {serve_fifteen_love} serve did not get returned. You are winning 30-0!")

    else:
        print("You did not win the toss. Your opponent chose to serve first.\nWould you like to start play on the north or south side of the court?")

        north_south = input("North or South > ").lower()

        print(f"Please make your way to the {north_south} side of the court and prepare to return the serve.")



else:
    spin = input("Up or Down > ").lower()

    spin_option = ['up', 'down']
    other_spin = random.choice(spin_option)




    if spin == other_spin:
        print("Congratulations, you won the toss. You get to choose whether to serve or receive.")

        serve_receive = input("Serve or Receive > ").lower()

        print(f"You chose to {serve_receive}. Here are the balls.")

        print("Below is a list of the possible serves to hit.")

        for serving_deuce in serve_options_deuce:
            print(f"> {serving_deuce}")
        serve_love_all = input("Which serve from above will you hit? ").lower()
        print(f"You hit a {serve_love_all} serve.")
        print("It was an ACE! You are winning 15-0.")

        for serving_ad in serve_options_ad:
            print(f"> {serving_ad}")
        serve_fifteen_love = input("The score is 15-0. Which serve from above will you hit next?")
        print(f"You hit a {serve_fifteen_love} serve.")
        print(f"Your {serve_fifteen_love} serve did not get returned. You are winning 30-0!")

    else:
        print("You did not win the toss. Your opponent chose to serve first.\nWould you like to start play on the north or south side of the court?")

        north_south = input("North or South > ").lower()

        print(f"Please make your way to the {north_south} side of the court and prepare to return the serve.")
