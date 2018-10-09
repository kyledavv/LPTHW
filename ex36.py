from sys import exit
import qprompt


def dead(why):
    print(120 * "-")
    print(why, "\nYou have failed. Now millions of lives are on your conscious.")
    print(120 * "-")
    exit(0)


def heaven():
    print(120 * "-")
    print("You now materialize into a calm and peaceful room with 2 doors. One on the left and one on the right.")
    print(120 * "-")

    heaven_choice = input("Which door do you choose: left or right? >").lower()

    if heaven_choice == "left":
        junie_4()
    elif heaven_choice == "right":
        ghost_5()
    else:
        heaven()


def amirah_0():
    print(120 * "-")
    print("""
    You have entered door number 1.
    When you enter, you smell something that makes you freeze in place.
    It smells like rotting meat for some reason. Then you look around and see...
    zombies infected with the Seif Al Din are all around you. Hundreds of them.
    But then you look down and see that you have a M4 Carbine with 4 extra magazines,
    a 9mm Beretta, and your 3.335 inch Wilson Rapid Response Folding Knife.
    What do you do?""")
    print(120 * "-")

    zombie_options = [
        'Full automatic fire, aiming for body shots',
        'Save the infected people',
        'Semi automatic fire, aiming for headshots only',
        'Run away'
    ]

    menu = qprompt.Menu()
    for i, item in enumerate(zombie_options):
        menu.add(str(i + 1), item)

    zombie_options_choice = menu.show()

    if zombie_options_choice == "1":
        dead("The zombies staggered, but did not fall. They surround you and tear your throat out.\n")
    elif zombie_options_choice == "2":
        dead("By putting your guard down and hesitating, the zombies launch on you and tear your throat out.\n")
    elif zombie_options_choice == "3":
        heaven()
    else:
        start()


def jakoby_1():
    print(120 * "-")
    print("You have entered door number 2.")
    print("There are four berserkers who turn to look at you with hatred in their eyes. ")
    print("You look down and see you have your 3.335 inch Wilson Rapid Response Folding Knife in your hand, with nothing else.")
    print("One of the berserkers roars, in a terrifyingly loud voice. \nThen everyone moves to attack.")
    print("What do you do?")
    print(120 * "-")

    berserker_options = [
        'Slash the knees',
        'Punch and slash their faces',
        'Drive the knife into their mouths',
        'Run'
    ]

    menu = qprompt.Menu()
    for i, item in enumerate(berserker_options):
        menu.add(str(i + 1), item)

    berserker_options_choice = menu.show()

    if berserker_options_choice == "1":
        dead("The berserker fell to one knee, but then punches you so hard that your sternum collapses into your heart, killing you instantly.")
    elif berserker_options_choice == "2":
        dead("The berserker's masks protect their faces from any blade or impact. They easily knock it off then tear off your arms.")
    elif berserker_options_choice == "3":
        heaven()
    elif berserker_options_choice == "4":
        start()
    else:
        jakoby_1()


def gault_2():
    print(120 * "-")
    print("""
    You have entered door number 3.
    You see Sebastian Gault, covered in bandages from his burns.
    Next to him is his faithful servant, Toys. There are numerous television
    screens behind them, showing hundreds of vials
    of the weaponized Ebola virus in different locations around the world.
    You then notice that Gault has a trigger device in his hand, that is set to
    deliver the weaponized Ebola to the world. Gault starts laughing, and moves to
    activate the trigger device.
    What do you do?
    """)
    print(120 * "-")

    gault_options = [
        'Double tap Gault and Toys in the head',
        'Shoot Gault in the hand, then in the head',
        'Beg them not to release the Ebola',
        'Run away'
    ]

    menu = qprompt.Menu()
    for i, item in enumerate(gault_options):
        menu.add(str(i + 1), item)

    gault_options_choice = menu.show()

    if gault_options_choice == "1":
        heaven()
    elif gault_options_choice == "2":
        heaven()
    elif gault_options_choice == "3":
        dead("Gault being the monster he is decides the world needs to die, so he presses the trigger device.")
    elif gault_options_choice == "4":
        start()
    else:
        gault_2()


def upier_3():
    print(120 * "-")
    print("""
    You have entered door number 4.
    You see Grigor sitting in his throne, smiling at you with an evil smile.
    There is live video of 8 nukes on screens placed around the tunnel.
    The three holy sites in the world, Jerusalem, Mecca, and the Vatican,
    are all on the screen with nukes sitting directly under them.
    Grigor has a cell phone in his hand, and reaches to press the call button to
    detonate the nukes.
    What do you do?
    """)
    print(120 * "-")

    upier_options = [
        'Tell Mr. Church to jam the signal so he cannot active the nukes',
        'Beat Grigor to a pulp.',
        'Shoot the phone in his hand',
        'Shoot Grigor in the head',
        'Sick Ghost on Grigor',
        'Run away'
    ]

    menu = qprompt.Menu()
    for i, item in enumerate(upier_options):
        menu.add(str(i + 1), item)

    upier_options_choice = menu.show()

    if upier_options_choice == "1":
        dead("You cannot get a signal up to Mr. Church. You are too far away.")
    elif upier_options_choice == "2":
        dead("Grigor still has a chance to detonate the nukes before he dies.")
    elif upier_options_choice == "3":
        dead("The phone had an auto detonate if it was tampered with in any way.")
    elif upier_options_choice == "4":
        heaven()
    elif upier_options_choice == "5":
        heaven()
    elif upier_options_choice == "6":
        start()
    else:
        upier_3


def junie_4():
    print(120 * "-")
    print("""
    You have entered the left door.
    Inside, you see Junie Flynn, the love of your life.
    She is cancer free, the world is saved, and you are at peace.
    She is sitting on the bed, giving you a warm smile. You go
    and sit next to her, and put your arms around her. Peace.
    """)
    print(120 * "-")
    exit(0)


def ghost_5():
    print(120 * "-")
    print("""
    You have entered the right door. Inside, you see Ghost.
    He is curled up on your bed, dreaming peacefully. You go to him
    and wrap your arms around him, while burying your face into his fur.
    Here is your best friend, your fellow warrior, and your rock.
    You feel the peace of having such a strong companion.
    """)
    print(120 * "-")
    exit(0)


def start():
    print(120 * "-")
    print("You materialize in the middle of a circular chamber. You can hear very loud thunder booming way overhead.")
    print("You have the feeling that you have just entered into hell.")
    print("You look around, and realize there are 4 doors spaced evenly around the circular chamber. ")
    print(120 * "-")

    door_options = [
        '1',
        '2',
        '3',
        '4',
    ]

    menu = qprompt.Menu()
    for i, item in enumerate(door_options):
        menu.add(str(i + 1), item)

    choice = menu.show()

    if choice == "1":
        amirah_0()
    elif choice == "2":
        jakoby_1()
    elif choice == "3":
        gault_2()
    elif choice == "4":
        upier_3()
    else:
        start()

start()
