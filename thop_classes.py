#!/usr/bin/env python
#############################################
#####-----A text based adventure--------#####
#####---------Object Oriented-----------#####
#####--------Modules and Classes--------#####
#############################################
#copyright derek thatcher 2013
#################################
#       #       #       #       #
#       |       |       |       #
# room7 # room8 # room9 # room10#
#       #       #       #       #
####################~#######~####
#       #       #       #       #
#       |       |       #       #
# room1 # room4 # room5 # room6 #
#       #       #       #       #
###-#######-################~####
#       #       #       #       #
#       |       |       #       #
# start # room2 # room3 # room11} finish
#       #       #       #       #
#################################

#imports
from string import lower
#############################################
#####------------room class-------------#####
#############################################
class room:
    def __init__(self):
        self.name = '', 
    
    def setup(self, name, items, characters, doors, text):
        self.name = name
        self.items = items #list of item
        self.characters = characters #list of character
        self.doors = doors #list of doors
        self.description = text

    def enter(self):
        print self.description
        if self.name == 'room12' and len(self.items) >= 0:
            if self.items[0].name == 'excalibur':
                print "In the centre of the room there is a sword embedded deep in a rock."
        if len(self.doors) >= 1:
            print "There is a door to",
            for d in self.doors:
                d.print_door()
        if len(self.items) >= 1:
            print "\nThere is",
            for i in self.items:
                i.print_item()
        if len(self.characters) >= 1:
            print "\nThere is",
            for c in self.characters:
                c.print_character()
        print "\n",

    def remove_item(self, item):
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)

#############################################
#####-------------item class------------#####
#############################################
class item:
    
    def __init__(self, name, canTake, isWeapon, power):
        self.name = name
        self.canTake = canTake #boolean
        self.isWeapon = isWeapon #boolean
        self.power = power

    def print_item(self):
        print "a %s," % self.name,
        
#############################################
#####-------------door class------------#####
#############################################
class door:
    
    def __init__(self, direction, door_to, locked, key):
        self.door_to = door_to #room that you walk through door to
        self.direction = direction #north, east, west or south
        self.locked = locked #boolean
        self.key = key #thing to unlock door

    def toggle_lock(self):
        self.locked = not self.locked
    
    def unlock(self, list):
        success = False
        for i in list:
            if self.key == i.name:
                self.locked = False
                print "You unlocked the %s door." % self.direction
                success = True
        if not success and self.locked:
            print "You do not have the key for the %s door." % self.direction

    def is_locked(self):
        return self.locked
    
    def isdoor(self,text):
        return self.direction in text

    def print_door(self):
        print "the %s," % self.direction,

#############################################
#####---------character class-----------#####
#############################################
class character:
    
    def __init__(self, name, attacking, talking, text, power):
        self.name = name
        self.attack = attacking #boolean
        self.talking = talking #boolean
        self.speech = text
        self.power = power
    
    def print_character(self):
        print "a %s," % self.name,
        if self.attack:
            print "he looks menacing,",

    def speak(self,user_input   ):
        if lower(self.name) in user_input and self.talking:
            print self.name, 'says', self.speech

    def fight(self, player):
        #returns True is character dies
        if not self.attack:
            print "You can not fight %s" % self.name
        else:
            if not player.hasweapon():
                print "You have no weapon. %s defeats you. You lose 25 health and 10 points." % self.name
                player.health -= 25
                player.points -= 10
            elif self.power < player.power():
                print "You defeat %s. You gain %s points." % (self.name, self.power)
                player.points += self.power
                player.bodycount += 1
                return True
            else:
                print "%s defeats you. You lose 25 health and 50 points." % self.name
                player.points -= 50
                player.health -= 25
        return False
#############################################
#####---------higescore class-----------#####
#############################################
import shelve
class highscore:
    def __init__(self):
        self.scores = []

    def save_score(self):
        if self.scores[0] == []:
            self.scores.remove(self.scores[0])
        self.scores.sort(key=lambda tup: tup[1]) 
        shelfFile = shelve.open('thop_savefile')
        shelfFile ['scores'] = self.scores
        shelfFile.close()
    
    def load_score(self):
        shelfFile = shelve.open('thop_savefile')
        self.scores = shelfFile ['scores']
        shelfFile.close()

    def add_score(self, name, score):
        self.scores.append((name,score))


    def print_score(self):
        #need to order list and format printing
        print "------------------------------------------"
        print " Top Ten High Scores"
        print "------------------------------------------"
        if len(self.scores)<=10:
            l = 0
        else:
            l = len(self.scores) - 11
        for n in range(len(self.scores)-1,l,-1):
            if len(self.scores[n])>1:
                print "Player %s scored %s points"%(self.scores[n][0],self.scores[n][1])



#############################################
#####-----------player class------------#####
#############################################
class player:
    
    def __init__(self, name, room):
        self.name = name
        self.health = 100 #percentage
        self.inventory = []
        self.inventory.append(item('lamp', True, False,0))
        self.location = room
        self.points = 0
        self.bodycount = 0

    def take(self, user_input):
        for i in self.location.items:
            if i.name in user_input:
                if i.canTake and len(self.inventory) < 6:
                    self.inventory.append(i)
                    print "You take a %s." % i.name
                    self.location.remove_item(i)
                elif i.canTake and len(self.inventory) >= 6:
                    print "You have no more room."
                else: print "You can't take that."

    def drop(self, user_input):
        success = False
        for i in self.inventory:
            if i.name in user_input:
                self.inventory.remove(i)
                self.location.add_item(i)
                print "You drop the ", i.name
                success = True
        if not success:
            print "You do not have that item to drop."


    def move(self, room):
        self.location = room
        #take point off each time you move rooms
        self.points -= 1

    def player_is_in_room(self, room):
        return self.location == room

    def hasweapon(self):
        for i in self.inventory:
            if i.isWeapon:
                return True
        return False
    
    def haslamp(self):
        for i in self.inventory:
            if i.name == 'lamp':
                return True
        return False

    def print_inventory(self):
        print "%ss inventory: " % self.name,
        for i in self.inventory:
            print "%s," % i.name,
        print

    def stats(self):
        print "Stats for %s: " % self.name
        print "------------------------------------------"
        print "Health: %s percent" % self.health
        print "Score: %s points" % self.points
        print "Power: %s " % self.power()
        print "Number of items in inventory: %s" % len(self.inventory)
        print "------------------------------------------"

    def power(self):
        #returns power of player
        ans = 0
        for i in self.inventory:
            ans += i.power
        #print "Bodycount: %s *50 +, Wepaons: %s + Health: %s" % (self.bodycount,ans,self.health)
        return self.bodycount*50+ans+self.health
