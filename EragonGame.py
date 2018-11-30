from sys import exit
from random import randint
from textwrap import dedent
import qprompt


class Scene(object):

    def __init__(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

    failure = [
                'You have failed.',
                'Eragon and Saphira have failed on their quest.',
                'The world is now doomed from your failure.',
                'The dragons will never be able to thrive again.',
                'Alagaesia will never be able to reborn the Riders.'
    ]

    def enter(self):
        print(120 * "-")
        print(Death.failure[randint(0, len(self.failure)-1)])
        print(120 * "-")
        exit(1)


class Start(Scene):

    def enter(self):
        print(120 * "-")
        print(dedent("""
                        You are Eragon Shadeslayer, riding atop your beloved
                        dragon, Saphira. You are leaving Alagaesia, and it is
                        up to you to find a new training/nesting place for
                        the hundreds of dragon eggs and Eldunari that you
                        have stowed with you.
                        You look down and see vast amounts of forestland
                        beneath you. From what you can see, there are
                        four quadrants that you and Saphira can explore
                        to find a nesting place for the dragon eggs. You
                        see a place to the North West, North, North East,
                        and a place on the distant horizon to the far North.
                        Which place do you choose to explore first?
                        """))
        print(120 * "-")

        prompt_start = [
                                'North West',
                                'North',
                                'North East',
                                'Far North'
                                ]

        menu = qprompt.Menu()
        for i, item in enumerate(prompt_start):
                menu.add(str(i + 1), item)

        prompt_start_choice = menu.show()

        if prompt_start_choice == "1":
            return 'elves'
        elif prompt_start_choice == "2":
            return 'trolls'
        elif prompt_start_choice == "3":
            return 'paradise'
        elif prompt_start_choice == "4":
            return 'dragon'
        else:
            return 'saphira'


class Saphira(Scene):

    def enter(self):
        print(120 * "-")
        print(dedent("""
                You and Saphira have successfully escaped back into the air
                above the forest. Saphira turns around and goes back to the
                starting point, where you have the options to go to the
                North West, North, North East, or far to the North.
                """))
        print(120 * "-")

        prompt_start = [
                        'North West',
                        'North',
                        'North East',
                        'Far North'
                        ]

        menu = qprompt.Menu()
        for i, item in enumerate(prompt_start):
            menu.add(str(i + 1), item)

        prompt_start_choice = menu.show()

        if prompt_start_choice == "1":
            return 'elves'
        elif prompt_start_choice == "2":
            return 'trolls'
        elif prompt_start_choice == "3":
            return 'paradise'
        elif prompt_start_choice == "4":
            return 'dragon'
        else:
            return 'saphira'


class Elves(Scene):

    def enter(self):
        print(120 * "-")
        print(dedent("""
                        You and Saphira land in the forest, and everything
                        instantly gets darker. You feel a presence all around
                        you, but can see nothing. All of a sudden, you see
                        movement all around you. You see twelve elves circling
                        you, all armed with swords, shields, and dark magic
                        around their hands. You and Saphira tense and prepare
                        yourself for the intensity of the moment.\n
                        All twelve elves instantly spring forward to attack.
                        What do you do?
                        """))

        print(120 * "-")
        prompt_elves = [
                        'Hop on Saphira and fly away',
                        'Pull out Brisingr and fight',
                        'Use one of the twelve words of killing',
                        'Speak in the Ancient Language that you are a friend',
                        'Use spell to make a bright white light to evade them',
                        'Gather the Eldunari\'s power to make a spell'
                        ]

        menu = qprompt.Menu()
        for i, item in enumerate(prompt_elves):
            menu.add(str(i + 1), item)

        prompt_elves_choice = menu.show()

        if prompt_elves_choice == "1":
            print(120 * "-")
            print("The elves get to you and Saphira before you can fly away.")
            print(120 * "-")
            return 'death'

        elif prompt_elves_choice == "2":
            print(120 * "-")
            print("The elves prove to be merciless fighters. You attempt\n")
            print("to fight, but they kill you and Saphira.")
            print(120 * "-")
            return 'dead'

        elif prompt_elves_choice == "3":
            print(120 * "-")
            print("While you are choosing which word to use, they swarm you\n")
            print("and kill you and Saphira.")
            print(120 * "-")
            return 'dead'

        elif prompt_elves_choice == "4":
            print(120 * "-")
            print("Even though you say you are a friend, they are not.\n")
            print("They kill you and Saphira.")
            print(120 * "-")
            return 'dead'

        elif prompt_elves_choice == "5":
            print(120 * "-")
            print("You use a spell to make blinding white light that freezes")
            print("the elves. That allows you to hop on Saphira and fly away")
            print(120 * "-")
            return 'saphira'

        elif prompt_elves_choice == "6":
            print(120 * "-")
            print("You summon a spell that freezes the elves, allowing you")
            print("and Saphira to escape unscathed.")
            print(120 * "-")
            return 'saphira'


class Trolls(Scene):

    def enter(self):
        print(120 * "-")
        print(dedent("""
                    You and Saphira land in the forest. You notice Saphira
                    tense as she smells something wrong. When Eragon uses his
                    elven senses to smell, he notices the smell of rotting
                    meat. They look around and see huge trolls in the clearing
                    next to where they landed. They notice you and start
                    walking towards you. What do you do?
                    """))
        print(120 * "-")
        prompt_trolls = [
                        'Attack with Brisingr and Saphira\'s claws',
                        'Have Saphira cook them with her fire',
                        'You speak to them saying you are a friend',
                        'You hop back on Saphira\'s back and fly away',
                        ]

        menu = qprompt.Menu()
        for i, item in enumerate(prompt_trolls):
            menu.add(str(i + 1), item)

        prompt_trolls_choice = menu.show()

        if prompt_trolls_choice == "1":
            print(120 * "-")
            print(dedent("""
                        The trolls tear you and Saphira apart. They are far too
                        strong and have too many of them for you to win.
                        You die.
                        """))
            print(120 * "-")
            return 'death'

        elif prompt_trolls_choice == "2":
            print(120 * "-")
            print(dedent("""
                        Cooking them starts to work at first, but then they
                        flank Saphira while she burns some of them. Sahpira
                        dies, followed by Eragon shortly after.
                        """))
            print(120 * "-")
            return 'death'

        elif prompt_trolls_choice == "3":
            print(120 * "-")
            print(dedent("""
                        They listen, and tell you that you must get off their
                        land or they will kill you. You and Saphira fly away.
                        """))
            print(120 * "-")
            return 'saphira'

        elif prompt_trolls_choice == "4":
            print(120 * "-")
            print(dedent("""
                        Eragon quickly jumps onto Saphira, and you fly away
                        to the trolls raising their clubs over their heads
                        while they bellow at you.
                        """))
            print(120 * "-")
            return 'saphira'


class Paradise(Scene):

    def enter(self):
        print(120 * "-")
        print(dedent("""
                    You and Saphira land in the middle of paradise. There is
                    a beautiful lake with rivers flowing out from it in 3
                    directions. You and Saphira share a thought that this
                    place is perfect. You land, and decide to make camp.
                    While you are eating, you and her are talking about
                    this place of paradise. What decision should they make?
                    """))
        print(120 * "-")
        prompt_paradise = [
                            'Stay and make this place home',
                            'Leave and discard it',
                            ]
        menu = qprompt.Menu()
        for i, item in enumerate(prompt_paradise):
            menu.add(str(i + 1), item)

        prompt_paradise_choice = menu.show()

        if prompt_paradise_choice == "1":
            print(120 * "-")
            print(dedent("""
                        You and Saphira are extremely excited that you finally
                        found the place to call home. You pick some plants to
                        eat and Saphira goes hunting. You eat dinner, talk,
                        and then fall asleep.
                        In the morning, you both wake up in terrible pain,
                        realizing you have somehow been poisoned. Eragon
                        goes in a cold sweat and dies before midafternoon.
                        Saphira roars and dies of the poison shortly after.
                        """))
            print(120 * "-")
            return 'death'

        elif prompt_paradise_choice == "2":
            print(120 * "-")
            print(dedent("""
                        You hop back up on Saphira and fly out over the forest
                        """))
            print(120 * "-")


class Dragon(Scene):

    def enter(self):
        print(120 * "-")
        print(dedent("""
                    You and Saphira fly down into a valley next to a mountain.
                    Everything is still, except for a slight breeze rustling
                    the trees. All of a sudden, you feel your mind start to
                    be penetrated by a weird consciousness. What do you do?
                    """))
        print(120 * "-")

        prompt_dragons = [
                        'Protect your barriers and fly away',
                        'Fight back with the Eldunari and Saphira\'s mind',
                        'Say that you are a friend in the ancient language'
                        ]

        menu = qprompt.Menu()
        for i, item in enumerate(prompt_dragons):
            menu.add(str(i + 1), item)

        prompt_dragons_choice = menu.show()

        if prompt_dragons_choice == "1":
            print(120 * "-")
            print(dedent("""
                        Saphira immediately flys off above the forest,
                        scared of the power of the consciousness.
                        """))
            print(120 * "-")
            return 'saphira'

        elif prompt_dragons_choice == "2":
            print(120 * "-")
            print(dedent("""
                        The Eldunari, Saphira, and you push with all your might
                        against the consciousness. Eventually, the
                        consciousness pushes back with such ferocity, that
                        it destroys all three of your barriers. A voice then
                        speaks in your mind, saying,\n
                        \"Welcome Eragon and Saphira, we have been expecting
                        you.\"
                        """))
            print(120 * "-")
            return 'finished'

        elif prompt_dragons_choice == "3":
            print(120 * "-")
            print(dedent("""
                        Eragon quickly shouts that he is a friend and rider,
                        looking for a new haven. A voice then speaks in his
                        mind, saying\n
                        \"Welcome Eragon and Saphira, we have been expecting
                        you.\"
                        """))


class Finished(Scene):

    def enter(self):
        print("You won! You have found the best place to train the Riders!")


class Map(object):

    scenes = {
                'start': Start(),
                'saphira': Saphira(),
                'elves': Elves(),
                'trolls': Trolls(),
                'paradise': Paradise(),
                'dragons': Dragon(),
                'death': Death(),
                'finished': Finished()
                }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('start')
a_game = Engine(a_map)
a_game.play()
