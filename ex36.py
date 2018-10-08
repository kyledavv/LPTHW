from sys import exit
import qprompt

def amirah_0():
    print("""
    You have entered door number 1.
    When you enter, you smell something that makes you freeze in place.
    It smells like rotting meat for some reason. Then you look around and see...
    zombies infected with the Seif Al Din are all around you. Hundreds of them.
    But then you look down and see that you have a M4 Carbine with 4 extra magazines,
    a 9mm Beretta, and your 3.335 inch Wilson Rapid Response Folding Knife.
    What do you do?""")

    zombie_options = [
        'Full automatic fire, aiming for body shots',
        'Save the infected people',
        'Semi automatic fire, aiming for headshots only',
        'Run away'
    ]

    menu = qprompt.Menu()
    for i, item in enumerate(zombie_options):
        menu.add(i + 1, item)

    choice = menu.show()

    if qprompt.choice == 1:
        dead("The zombies staggered, but did not fall. They surround you and tear your throat out.\n")
    elif qprompt.choice == 2:
        dead("By putting your guard down and hesitating, the zombies launch on you and tear your throat out.\n")
    elif qprompt.choice == 3:
        heaven()
    else:
        start()






amirah_0()

def jakoby_1():
    print("You have entered door number 2.")
    print("There are four berserkers who turn to look at you with hatred in their eyes. ")
    print("You look down and see you have your 3.335 inch Wilson Rapid Response Folding Knife in your hand, with nothing else.")
    print("One of the berserkers roars, in a terrifyingly loud voice. \nThen everyone moves to attack.")

    berserker_options = [
        'Slash the knees',
        'Punch and slash their faces',
        'Drive the knife into their mouths',
        'Run'
    ]


#def gault_2():


#def upier_3():


#def alien_4():


#def bliss_5():


#def seven_kings_6():


#def nico_7():


#def junie_8():


#def ghost_9():


def dead(why):
    print(why, "You have failed. Now millions of lives are on your conscious.")
    exit(0)


def heaven():
    print("You now materialize into a calm and peaceful room with 2 doors. One on the left and one on the right.")

    heaven_choice = input("Which door do you choose: left or right? >").lower()

    if heaven_choice == "left":
        junie_8()
    elif heaven_choice == "right":
        ghost_9()
    else:
        heaven()



def start():
    print("You materialize in the middle of a circular chamber. You can hear very loud thunder booming way overhead. \nYou have the feeling that you have just entered into hell.")
    print("You look around, and realize there are 8 doors spaced evenly around the circular chamber. ")

    door_options = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
    ]

    menu = qprompt.Menu()
    for i, item in enumerate(door_options):
        menu.add(i + 1, item)

    choice = menu.show()
