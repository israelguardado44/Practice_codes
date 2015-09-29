class Scene(object):

    def __init__(self):
        pass
        
    def enter(self):
        pass

class Engine(object):

    
    def __init__(self, current_scene):
        self.current_scene = current_scene
        
    def play(self):
        self.current_scene.enter()

        print 'Where do you want to go?'
        print '1. Move forward'
        print '2. Move to the right'
        print '3. Move back'
        print '4. Move to the left'

        direction = int(raw_input('> '))
        while direction not in range(1,5):
            print '\nType a number 1-4'
            print 'Where do you want to go?'
            print '1. Move forward'
            print '2. Move to the right'
            print '3. Move back'
            print '4. Move to the left'
            direction = int(raw_input('> '))
        

        self.current_scene.exit(direction)


    def battle(self):
        for i in range(1, len(self.current_scene.enemies)+1):
            print str(i) + '.', self.current_scene.enemies[i-1]
        choice = int(raw_input('Choose your opponent: '))
        while choice not in range(1, len(self.current_scene.enemies)+1):
            print '\nType an number from the list idiot'
            for i in range(1, len(self.current_scene.enemies)+1):
                print str(i) + '.', self.current_scene.enemies[i-1]
            choice = int(raw_input('Choose your opponent: '))
        enemy = self.current_scene.enemies[choice - 1]

            
        


class Death(Scene):

    def enter(self):

        print 'Crap... you took a wrong turn an anvil fell on your head, and you died.'
        print "You're an idiot"

class CentralCorridor(Scene):

    def enter(self):
        print 'You are in the central corridor.'
        print 'There is a room to the right'
        print 'There is a room to straight ahead'

    def exit(self, direction):

        self.direction = direction
        if self.direction == 1:
            play_game = Engine(TheBridge())
            play_game.play()
        elif self.direction == 2:
            play_game = Engine(LaserWeaponArmory())
            play_game.play()
            

class LaserWeaponArmory(Scene):

    
    def __init__(self):
        pass

    def enter(self):
        print 'You have entered the Weapon armory'
        print 'The Central corridor is to the left'

    def exit(self, direction):

        self.direction = direction
        if self.direction == 4:
            play_game = Engine(CentralCorridor())
            play_game.play()
        else:
            print 'Choose a different direction'

class TheBridge(Scene):

    enemies = ['Bob: The destroyer of worlds and the wrecker of your sh**t', 'test henchman # 5']
    scene_items = ['The escape room key']

    def __init__(self):
        self.current_scene = 'The Bridge'

    def enter(self):
        print 'You have entered the Bridge'
        
        print "Enemies:"
        for enemy in self.enemies:
            print '\t', enemy


class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

class Player(object):

    def __init__(self):
        self.life = 10
        self.attack_dict = {'punch': 2, 'kick': 4, 'gun': 6}
        self.item = {'stuff': 0}

    def status(self):
        print 'Life: ', self.life
        print 'Item: ', self.item






play_game = Engine(CentralCorridor())
play_game.play()
