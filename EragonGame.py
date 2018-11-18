from sys import exit
from random import randint
from textwrap import dedent
import qprompt


class Scene(object):

    def __init__(self):

        menu = qprompt.Menu()
        for i, item in enumerate(self.prompt_options):
            menu.add(str(i + 1), item)


class Engine(object):

    var1 = 8

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
        print(Death.failure[randint(0, len(self.failure)-1)])
        exit(1)


class Saphira(Scene):

    def enter(self):
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

    prompt_options = [
                      'North West',
                      'North',
                      'North East',
                      'Far North'
        ]


class Elves(Scene):

    def enter(self):
        print(dedent("""
                        Elves text goes here
                    """))


class Trolls(Scene):

    def enter(self):
        pass


class Paradise(Scene):

    def enter(self):
        pass


class Dragon(Scene):

    def enter(self):
        pass


class Finished(Scene):

    def enter(self):
        print("You won! You have found the best place to train the Riders!")


class Map(object):

    scenes = {
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


a_map = Map('saphira')
a_game = Engine(a_map)
a_game.play()
